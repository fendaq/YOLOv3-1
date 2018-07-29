class Model_defs(object):
    tiny_model_defs = [
        {'type':'Conv',
         'n_fiter':16,
         'kernel':3,
         'stride':1,
         'pad':1,
         'bn': True,
         'act':'leaky',
        },
        {'type':'maxpool',
         'kernel':2,
         'stride':2,
        },
        {'type':'Conv',
         'n_fiter':32,
         'kernel':3,
         'stride':1,
         'pad':1,
         'bn': True,
         'act':'leaky',
        },
        {'type':'maxpool',
         'kernel':2,
         'stride':2,
        },
        {'type':'Conv',
         'n_fiter':64,
         'kernel':3,
         'stride':1,
         'pad':1,
         'bn': True,
         'act':'leaky',
        },
        {'type':'maxpool',
         'kernel':2,
         'stride':2,
        },
        {'type':'Conv',
         'n_fiter':128,
         'kernel':3,
         'stride':1,
         'pad':1,
         'bn': True,
         'act':'leaky',
        },
        {'type':'maxpool',
         'kernel':2,
         'stride':2,
        },
        {'type':'Conv',
         'n_fiter':256,
         'kernel':3,
         'stride':1,
         'pad':1,
         'bn': True,
         'act':'leaky',
        },
        {'type':'maxpool',
         'kernel':2,
         'stride':2,
        },
        {'type':'Conv',
         'n_fiter':512,
         'kernel':3,
         'stride':1,
         'pad':1,
         'bn': True,
         'act':'leaky',
        },
#         {'type':'maxpool',
#          'kernel':2,
#          'stride':1,
#         },

        {'type':'Conv',
         'n_fiter':1024,
         'kernel':3,
         'stride':1,
         'pad':1,
         'bn': True,
         'act':'leaky',
        },
        
        ###################
        
        {'type':'Conv',
         'n_fiter':256,
         'kernel':1,
         'stride':1,
         'pad':1,
         'bn': True,
         'act':'leaky',
        },
        {'type':'Conv',
         'n_fiter':512,
         'kernel':3,
         'stride':1,
         'pad':1,
         'bn': True,
         'act':'leaky',
        },
        {'type':'Conv',
         'n_fiter':255,
         'kernel':1,
         'stride':1,
         'pad':1,
         'bn': False,
         'act':'linear',
        },
        {'type':'yolo',
         'mask':[3,4,5],
         'anchors':[10,14,  23,27,  37,58,  81,82,  135,169,  344,319],
         'classes':80,
         'num':6,
         'jitter':.3,
         'ignore_thresh': .7,
         'truth_thresh': 1,
         'random':1   # or true?
        },
        {'type':'route',
         'layers':[-4],   
        },
        {'type':'Conv',
         'n_fiter':128,
         'kernel':1,
         'stride':1,
         'pad':1,
         'bn': True,
         'act':'leaky',
        },
        {'type':'upsample',
         'stride':2,
        },
        {'type':'route',
         'layers':[-1, 7],   
        },
        {'type':'Conv',
         'n_fiter':256,
         'kernel':3,
         'stride':1,
         'pad':1,
         'bn': True,
         'act':'leaky',
        },
        {'type':'Conv',
         'n_fiter':255,
         'kernel':1,
         'stride':1,
         'pad':1,
         'bn': False,
         'act':'linear',
        },
        {'type':'yolo',
         'mask':[1,2,3],
         'anchors':[10,14,  23,27,  37,58,  81,82,  135,169,  344,319],
         'classes':80,
         'num':6,
         'jitter':.3,
         'ignore_thresh': .7,
         'truth_thresh': 1,
         'random':1   # or true?
        },
    ]
    model_defs = [
        {'type':'Conv',
         'n_fiter':32,
         'kernel':3,
         'stride':1,
         'pad':1,
         'bn': True,
         'act':'leaky',
        },
        {'type':'Conv',
         'n_fiter':64,
         'kernel':3,
         'stride':2,
         'pad':1,
         'bn': True,
         'act':'leaky',
        },
        {'type':'Conv',
         'n_fiter':32,
         'kernel':1,
         'stride':1,
         'pad':1,
         'bn': True,
         'act':'leaky',
        },
        {'type':'Conv',
         'n_fiter':64,
         'kernel':3,
         'stride':1,
         'pad':1,
         'bn': True,
         'act':'leaky',
        },
        {'type':'shortcut',
         'from':-3,
        },
        {'type':'Conv',
         'n_fiter':128,
         'kernel':3,
         'stride':2,
         'pad':1,
         'bn': True,
         'act':'leaky',
        },
        {'type':'Conv',
         'n_fiter':64,
         'kernel':1,
         'stride':1,
         'pad':1,
         'bn': True,
         'act':'leaky',
        },
        {'type':'Conv',
         'n_fiter':128,
         'kernel':3,
         'stride':1,
         'pad':1,
         'bn': True,
         'act':'leaky',
        },
        {'type':'shortcut',
         'from':-3,
        },
        {'type':'Conv',
         'n_fiter':64,
         'kernel':1,
         'stride':1,
         'pad':1,
         'bn': True,
         'act':'leaky',
        },
        {'type':'Conv',
         'n_fiter':128,
         'kernel':3,
         'stride':1,
         'pad':1,
         'bn': True,
         'act':'leaky',
        },
        {'type':'shortcut',
         'from':-3,
        },
        {'type':'Conv',
         'n_fiter':256,
         'kernel':3,
         'stride':2,
         'pad':1,
         'bn': True,
         'act':'leaky',
        },
        {'type':'Conv',
         'n_fiter':128,
         'kernel':1,
         'stride':1,
         'pad':1,
         'bn': True,
         'act':'leaky',
        },
        {'type':'Conv',
         'n_fiter':256,
         'kernel':3,
         'stride':1,
         'pad':1,
         'bn': True,
         'act':'leaky',
        },
        {'type':'shortcut',
         'from':-3,
        },
        {'type':'Conv',
         'n_fiter':128,
         'kernel':1,
         'stride':1,
         'pad':1,
         'bn': True,
         'act':'leaky',
        },
        {'type':'Conv',
         'n_fiter':256,
         'kernel':3,
         'stride':1,
         'pad':1,
         'bn': True,
         'act':'leaky',
        },
        {'type':'shortcut',
         'from':-3,
        },
        {'type':'Conv',
         'n_fiter':128,
         'kernel':1,
         'stride':1,
         'pad':1,
         'bn': True,
         'act':'leaky',
        },
        {'type':'Conv',
         'n_fiter':256,
         'kernel':3,
         'stride':1,
         'pad':1,
         'bn': True,
         'act':'leaky',
        },
        {'type':'shortcut',
         'from':-3,
        },
        {'type':'Conv',
         'n_fiter':128,
         'kernel':1,
         'stride':1,
         'pad':1,
         'bn': True,
         'act':'leaky',
        },
        {'type':'Conv',
         'n_fiter':256,
         'kernel':3,
         'stride':1,
         'pad':1,
         'bn': True,
         'act':'leaky',
        },
        {'type':'shortcut',
         'from':-3,
        },
        {'type':'Conv',
         'n_fiter':128,
         'kernel':1,
         'stride':1,
         'pad':1,
         'bn': True,
         'act':'leaky',
        },
        {'type':'Conv',
         'n_fiter':256,
         'kernel':3,
         'stride':1,
         'pad':1,
         'bn': True,
         'act':'leaky',
        },
        {'type':'shortcut',
         'from':-3,
        },
        {'type':'Conv',
         'n_fiter':128,
         'kernel':1,
         'stride':1,
         'pad':1,
         'bn': True,
         'act':'leaky',
        },
        {'type':'Conv',
         'n_fiter':256,
         'kernel':3,
         'stride':1,
         'pad':1,
         'bn': True,
         'act':'leaky',
        },
        {'type':'shortcut',
         'from':-3,
        },
        {'type':'Conv',
         'n_fiter':128,
         'kernel':1,
         'stride':1,
         'pad':1,
         'bn': True,
         'act':'leaky',
        },
        {'type':'Conv',
         'n_fiter':256,
         'kernel':3,
         'stride':1,
         'pad':1,
         'bn': True,
         'act':'leaky',
        },
        {'type':'shortcut',
         'from':-3,
        },
        {'type':'Conv',
         'n_fiter':128,
         'kernel':1,
         'stride':1,
         'pad':1,
         'bn': True,
         'act':'leaky',
        },
        {'type':'Conv',
         'n_fiter':256,
         'kernel':3,
         'stride':1,
         'pad':1,
         'bn': True,
         'act':'leaky',
        },
        {'type':'shortcut',
         'from':-3,
        },
        {'type':'Conv',
         'n_fiter':512,
         'kernel':3,
         'stride':2,
         'pad':1,
         'bn': True,
         'act':'leaky',
        },
        {'type':'Conv',
         'n_fiter':256,
         'kernel':1,
         'stride':1,
         'pad':1,
         'bn': True,
         'act':'leaky',
        },
        {'type':'Conv',
         'n_fiter':512,
         'kernel':3,
         'stride':1,
         'pad':1,
         'bn': True,
         'act':'leaky',
        },
        {'type':'shortcut',
         'from':-3,
        },
        {'type':'Conv',
         'n_fiter':256,
         'kernel':1,
         'stride':1,
         'pad':1,
         'bn': True,
         'act':'leaky',
        },
        {'type':'Conv',
         'n_fiter':512,
         'kernel':3,
         'stride':1,
         'pad':1,
         'bn': True,
         'act':'leaky',
        },
        {'type':'shortcut',
         'from':-3,
        },
        {'type':'Conv',
         'n_fiter':256,
         'kernel':1,
         'stride':1,
         'pad':1,
         'bn': True,
         'act':'leaky',
        },
        {'type':'Conv',
         'n_fiter':512,
         'kernel':3,
         'stride':1,
         'pad':1,
         'bn': True,
         'act':'leaky',
        },
        {'type':'shortcut',
         'from':-3,
        },
        {'type':'Conv',
         'n_fiter':256,
         'kernel':1,
         'stride':1,
         'pad':1,
         'bn': True,
         'act':'leaky',
        },
        {'type':'Conv',
         'n_fiter':512,
         'kernel':3,
         'stride':1,
         'pad':1,
         'bn': True,
         'act':'leaky',
        },
        {'type':'shortcut',
         'from':-3,
        },
        {'type':'Conv',
         'n_fiter':256,
         'kernel':1,
         'stride':1,
         'pad':1,
         'bn': True,
         'act':'leaky',
        },
        {'type':'Conv',
         'n_fiter':512,
         'kernel':3,
         'stride':1,
         'pad':1,
         'bn': True,
         'act':'leaky',
        },
        {'type':'shortcut',
         'from':-3,
        },
        {'type':'Conv',
         'n_fiter':256,
         'kernel':1,
         'stride':1,
         'pad':1,
         'bn': True,
         'act':'leaky',
        },
        {'type':'Conv',
         'n_fiter':512,
         'kernel':3,
         'stride':1,
         'pad':1,
         'bn': True,
         'act':'leaky',
        },
        {'type':'shortcut',
         'from':-3,
        },
        {'type':'Conv',
         'n_fiter':256,
         'kernel':1,
         'stride':1,
         'pad':1,
         'bn': True,
         'act':'leaky',
        },
        {'type':'Conv',
         'n_fiter':512,
         'kernel':3,
         'stride':1,
         'pad':1,
         'bn': True,
         'act':'leaky',
        },
        {'type':'shortcut',
         'from':-3,
        },
        {'type':'Conv',
         'n_fiter':256,
         'kernel':1,
         'stride':1,
         'pad':1,
         'bn': True,
         'act':'leaky',
        },
        {'type':'Conv',
         'n_fiter':512,
         'kernel':3,
         'stride':1,
         'pad':1,
         'bn': True,
         'act':'leaky',
        },
        {'type':'shortcut',
         'from':-3,
        },

        {'type':'Conv',
         'n_fiter':1024,
         'kernel':3,
         'stride':2,
         'pad':1,
         'bn': True,
         'act':'leaky',
        },
        {'type':'Conv',
         'n_fiter':512,
         'kernel':1,
         'stride':1,
         'pad':1,
         'bn': True,
         'act':'leaky',
        },
        {'type':'Conv',
         'n_fiter':1024,
         'kernel':3,
         'stride':1,
         'pad':1,
         'bn': True,
         'act':'leaky',
        },
        {'type':'shortcut',
         'from':-3,
        },

        {'type':'Conv',
         'n_fiter':512,
         'kernel':1,
         'stride':1,
         'pad':1,
         'bn': True,
         'act':'leaky',
        },
        {'type':'Conv',
         'n_fiter':1024,
         'kernel':3,
         'stride':1,
         'pad':1,
         'bn': True,
         'act':'leaky',
        },
        {'type':'shortcut',
         'from':-3,
        },

        {'type':'Conv',
         'n_fiter':512,
         'kernel':1,
         'stride':1,
         'pad':1,
         'bn': True,
         'act':'leaky',
        },
        {'type':'Conv',
         'n_fiter':1024,
         'kernel':3,
         'stride':1,
         'pad':1,
         'bn': True,
         'act':'leaky',
        },
        {'type':'shortcut',
         'from':-3,
        },

        {'type':'Conv',
         'n_fiter':512,
         'kernel':1,
         'stride':1,
         'pad':1,
         'bn': True,
         'act':'leaky',
        },
        {'type':'Conv',
         'n_fiter':1024,
         'kernel':3,
         'stride':1,
         'pad':1,
         'bn': True,
         'act':'leaky',
        },
        {'type':'shortcut',
         'from':-3,
        },

        {'type':'Conv',
         'n_fiter':512,
         'kernel':1,
         'stride':1,
         'pad':1,
         'bn': True,
         'act':'leaky',
        },
        {'type':'Conv',
         'n_fiter':1024,
         'kernel':3,
         'stride':1,
         'pad':1,
         'bn': True,
         'act':'leaky',
        },
        {'type':'Conv',
         'n_fiter':512,
         'kernel':1,
         'stride':1,
         'pad':1,
         'bn': True,
         'act':'leaky',
        },
        {'type':'Conv',
         'n_fiter':1024,
         'kernel':3,
         'stride':1,
         'pad':1,
         'bn': True,
         'act':'leaky',
        },
        {'type':'Conv',
         'n_fiter':512,
         'kernel':1,
         'stride':1,
         'pad':1,
         'bn': True,
         'act':'leaky',
        },
        {'type':'Conv',
         'n_fiter':1024,
         'kernel':3,
         'stride':1,
         'pad':1,
         'bn': True,
         'act':'leaky',
        },
        {'type':'Conv',
         'n_fiter':255,
         'kernel':3,
         'stride':1,
         'pad':1,
         'bn': False,
         'act':'linear',
        },
        ####### First yolo #########
        {'type':'yolo',
         'mask':[6,7,8],
         'anchors':[10,13,  16,30,  33,23,  30,61,  62,45,  59,119,  116,90,  156,198,  373,326],
         'classes':80,
         'num':9,
         'jitter':.3,
         'ignore_thresh': .7,
         'truth_thresh': 1,
         'random':1   # or true?
        },

        {'type':'route',
         'layers':[-4],   
        },

        {'type':'Conv',
         'n_fiter':256,
         'kernel':1,
         'stride':1,
         'pad':1,
         'bn': True,
         'act':'leaky',
        },

        {'type':'upsample', # Use pixelshuffle to replace it?
         'stride':2,
        },

        {'type':'route',
         'layers':[-1,61],   
        },

        {'type':'Conv',
         'n_fiter':256,
         'kernel':1,
         'stride':1,
         'pad':1,
         'bn': True,
         'act':'leaky',
        },

        {'type':'Conv',
         'n_fiter':512,
         'kernel':3,
         'stride':1,
         'pad':1,
         'bn': True,
         'act':'leaky',
        },

        {'type':'Conv',
         'n_fiter':256,
         'kernel':1,
         'stride':1,
         'pad':1,
         'bn': True,
         'act':'leaky',
        },

        {'type':'Conv',
         'n_fiter':512,
         'kernel':3,
         'stride':1,
         'pad':1,
         'bn': True,
         'act':'leaky',
        },
        {'type':'Conv',
         'n_fiter':256,
         'kernel':1,
         'stride':1,
         'pad':1,
         'bn': True,
         'act':'leaky',
        },

        {'type':'Conv',
         'n_fiter':512,
         'kernel':3,
         'stride':1,
         'pad':1,
         'bn': True,
         'act':'leaky',
        },
        {'type':'Conv',
         'n_fiter':255,
         'kernel':1,
         'stride':1,
         'pad':1,
         'bn': False,
         'act':'linear',
        },

        {'type':'yolo',
         'mask':[3,4,5],
         'anchors':[10,13,  16,30,  33,23,  30,61,  62,45,  59,119,  116,90,  156,198,  373,326],
         'classes':80,
         'num':9,
         'jitter':.3,
         'ignore_thresh':.7,
         'truth_thresh':1,
         'random':1,   
        },
        {'type':'route',
         'layers':[-4],   
        },
        {'type':'Conv',
         'n_fiter':128,
         'kernel':1,
         'stride':1,
         'pad':1,
         'bn': True,
         'act':'leaky',
        },

        {'type':'upsample', # Use pixelshuffle to replace it?
         'stride':2,
        },

        {'type':'route',
         'layers':[-1,36],   
        },

        {'type':'Conv',
         'n_fiter':128,
         'kernel':1,
         'stride':1,
         'pad':1,
         'bn': True,
         'act':'leaky',
        },

        {'type':'Conv',
         'n_fiter':256,
         'kernel':3,
         'stride':1,
         'pad':1,
         'bn': True,
         'act':'leaky',
        },

        {'type':'Conv',
         'n_fiter':128,
         'kernel':1,
         'stride':1,
         'pad':1,
         'bn': True,
         'act':'leaky',
        },

        {'type':'Conv',
         'n_fiter':256,
         'kernel':3,
         'stride':1,
         'pad':1,
         'bn': True,
         'act':'leaky',
        },

        {'type':'Conv',
         'n_fiter':128,
         'kernel':1,
         'stride':1,
         'pad':1,
         'bn': True,
         'act':'leaky',
        },

        {'type':'Conv',
         'n_fiter':256,
         'kernel':3,
         'stride':1,
         'pad':1,
         'bn': True,
         'act':'leaky',
        },

        {'type':'Conv',
         'n_fiter':255,
         'kernel':1,
         'stride':1,
         'pad':1,
         'bn': False,
         'act':'linear',
        },

        {'type':'yolo',
         'mask':[0,1,2],
         'anchors':[10,13,  16,30,  33,23,  30,61,  62,45,  59,119,  116,90,  156,198,  373,326],
         'classes':80,
         'num':9,
         'jitter':.3,
         'ignore_thresh':.7,
         'truth_thresh':1,
         'random':1,   
        },    
        ]

