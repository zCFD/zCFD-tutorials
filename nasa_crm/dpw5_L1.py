
import zutil

alpha = 2.21

def my_transform(x,y,z):
    v = [x,y,z]
    v =  zutil.rotate_vector(v,alpha,0.0)
    return {'v1' : v[0], 'v2' : v[1], 'v3' : v[2]}

parameters = {

 # units for dimensional quantities
'units' : 'SI',

# reference state
'reference' : 'IC_1',

'restart' : False,

'time marching' : {
                   'unsteady' : {
                                 'total time' : 1.0,
                                 'time step' : 1.0,
                                 'order' : 'second',
                                },
                   'scheme' : {
                               'name' : 'runge kutta',
                               'stage': 5,
                               },
                   'multigrid' : 3,
                    'multigrid cycles' : 20,
                   'cfl': 2.5,
                   'cfl transport': 1.0,
                   'cfl coarse': 1.0,
                   'cfl ramp factor': { 'initial': 1.0, 'growth': 1.1 },
                   'cycles' : 10000,
                  },

'equations' : 'RANS',

'RANS' : {
               'order' : 'euler_second',
               'limiter' : 'vanalbada',
               'precondition' : True,
               'turbulence' : {
                               'model' : 'sst',
                              },
               },

'material' : 'air',
'air' : {
        'gamma' : 1.4,
        'gas constant' : 287.0,
        'Sutherlands const': 110.4,
        'Prandtl No' : 0.72,
        'Turbulent Prandtl No' : 0.9,
        },
'IC_1' : {
          'temperature':310.928,
          'pressure':101325.0,
          'V': {
                'vector' : zutil.vector_from_angle(alpha,0.0),
                'Mach' : 0.85,
                },
           'Reynolds No' : 5.0e6,
           'Reference Length' : 275.8,
          'turbulence intensity':1.e-4,
          'eddy viscosity ratio':0.1,
          'ambient turbulence intensity':1.e-4,
          'ambient eddy viscosity ratio':0.1,
          },
'BC_1' : {
          'ref' : 7,
          'type' : 'symmetry',
         },
'BC_2' : {
          'ref' : 3,
          'type' : 'wall',
          'kind' : 'noslip',
         },
'BC_3' : {
          'ref' : 9,
          'type' : 'farfield',
          'condition' : 'IC_1',
          'kind' : 'riemann',
         },
'write output' : {
                  'format' : 'vtk',
                  'surface variables': ['p','T','rho','walldist','yplus','cp','pressureforce','frictionforce'],
                  'volume variables': ['V','p','T','rho','walldist','mach','cp','eddy'],
                  'frequency' : 500,
                 },
'report' : {
           'frequency' : 10,
        'forces' : {
            'FR_1' : {
                'name' : 'wall',
                'zone' : [9,10,11,12,13],
                'transform' : my_transform,
                'reference area' : 594720.0*0.5, # half model area # half model area # half model area
            },
        },
},
}
