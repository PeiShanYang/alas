config = {
    "ConfigAugmentation": {
        "AugmentationPara": {
            "randomHorizontalFlip": {
                "probability": {
                    "type": "flaot",
                    "default": 0.5,
                    "max": 1,
                    "min": 0
                }
            },
            "randomVerticalFlip": {
                "probability": {
                    "type": "flaot",
                    "default": 0.5,
                    "max": 1,
                    "min": 0
                }
            },
            "randomRotation": {
                "degrees": {
                    "children": {
                        "min": {
                            "type": "float",
                            "default": -360,
                            "max": 360,
                            "min": -360,
                        },
                        "max": {
                            "type": "float",
                            "default": 360,
                            "max": 360,
                            "min": -360,
                        }
                    }
                }
            },
            "randomTranslate": {
                "translate": {
                    "children": {
                        "horizontalRatio": {
                            "type": "float",
                            "default": 0,
                            "max": 1,
                            "min": 0,
                        },
                        "verticalRatio": {
                            "type": "float",
                            "default": 0,
                            "max": 1,
                            "min": 0,
                        }
                    }
                }
            },
            "randomScale": {
                "scale": {
                    "children": {
                        "horizontalRatio": {
                            "type": "float",
                            "default": 0,
                            "max": 1,
                            "min": 0,
                        },
                        "verticalRatio": {
                            "type": "float",
                            "default": 0,
                            "max": 1,
                            "min": 0,
                        }
                    }
                }
            },
            "randomShear": {
                "shear": {
                    "children": {
                        "horizontalDegreeMin": {
                            "type": "float",
                            "default": -360,
                            "max": 360,
                            "min": -360,
                        },
                        "horizontalDegreeMax": {
                            "type": "float",
                            "default": 360,
                            "max": 360,
                            "min": -360,
                        },
                        "verticalDegreeMin": {
                            "type": "float",
                            "default": -360,
                            "max": 360,
                            "min": -360,
                        },
                        "verticalDegreeMax": {
                            "type": "float",
                            "default": 360,
                            "max": 360,
                            "min": -360,
                        }
                    }
                }
            },
            "randomGrayscale": {
                "probability": {
                    "type": "flaot",
                    "default": 0.5,
                    "max": 1,
                    "min": 0
                }
            },
            "randomBrightness": {
                "brightnessRange": {
                    "children": {
                        "min": {
                            "type": "float",
                            "default": 1,
                            "min": 0,
                        },
                        "max": {
                            "type": "float",
                            "default": 1,
                            "min": 0,
                        }
                    }
                }
            },
            "randomContrast": {
                "contrast": {
                    "children": {
                        "min": {
                            "type": "float",
                            "default": 1,
                            "min": 0,
                        },
                        "max": {
                            "type": "float",
                            "default": 1,
                            "min": 0,
                        }
                    }
                }
            },
            "randomSaturation": {
                "saturation": {
                    "children": {
                        "min": {
                            "type": "float",
                            "default": 1,
                            "min": 0,
                        },
                        "max": {
                            "type": "float",
                            "default": 1,
                            "min": 0,
                        }
                    }
                }
            },
            "randomHue": {
                "hue": {
                    "children": {
                        "min": {
                            "type": "float",
                            "default": 0,
                            "max": 0.5,
                            "min": -0.5,
                        },
                        "max": {
                            "type": "float",
                            "default": 0,
                            "max": 0.5,
                            "min": -0.5,
                        }
                    }
                }
            },
            "randomErasing": {
                "probability": {
                    "type": "flaot",
                    "default": 0.5,
                    "max": 1,
                    "min": 0
                },
                "scale": {
                    "children": {
                        "min": {
                            "type": "float",
                            "default": 0.02,
                            "max": 1,
                            "min": 0,
                        },
                        "max": {
                            "type": "float",
                            "default": 0.33,
                            "max": 1,
                            "min": 0,
                        }
                    }
                },
                "ratio": {
                    "children": {
                        "min": {
                            "type": "float",
                            "default": 0.3,
                            "min": 0,
                        },
                        "max": {
                            "type": "float",
                            "default": 3.3,
                            "min": 0,
                        }
                    }
                },
                "value": {
                    "children": {
                        "R": {
                            "type": "int",
                            "default": 0,
                            "max": 255,
                            "min": 0,
                        },
                        "G": {
                            "type": "int",
                            "default": 0,
                            "max": 255,
                            "min": 0,
                        },
                        "B": {
                            "type": "int",
                            "default": 0,
                            "max": 255,
                            "min": 0,
                        }
                    }
                }
            },
            "randomPerspective": {
                "distortion": {
                    "type": "float",
                    "default": 0,
                    "max": 1,
                    "min": 0
                },
                "probability": {
                    "type": "flaot",
                    "default": 0.5,
                    "max": 1,
                    "min": 0
                },
                "interpolation": {
                    "type": "string",
                    "default": "BILINEAR",
                    "enums": {
                        "BILINEAR": "BILINEAR",
                        "NEAREST": "NEAREST",
                        "BICUBIC": "BICUBIC"
                    }
                },
                "fill": {
                    "children": {
                        "R": {
                            "type": "int",
                            "default": 0,
                            "max": 255,
                            "min": 0,
                        },
                        "G": {
                            "type": "int",
                            "default": 0,
                            "max": 255,
                            "min": 0,
                        },
                        "B": {
                            "type": "int",
                            "default": 0,
                            "max": 255,
                            "min": 0,
                        }
                    }
                }
            }
        }
    },
    "ConfigEvaluation": {
        "EvaluationPara": {
            "showAcc": {
                "switch": {
                    "type": "boolean",
                    "default": True
                }
            },
            "showClassAcc": {
                "switch": {
                    "type": "boolean",
                    "default": True
                }
            },
            "showNumOfClasses": {
                "switch": {
                    "type": "boolean",
                    "default": False
                }
            },
            "showWrongFile": {
                "switch": {
                    "type": "boolean",
                    "default": False
                }
            }
        }
    },
    "ConfigModelService": {
        "LossFunctionPara": {
            "lossFunction": {
                "type": "string",
                "default": "CrossEntropyLoss",
                "enums": {
                    "CrossEntropyLoss": "CrossEntropyLoss",
                    "MSELoss": "MSELoss",
                    "L1Loss": "L1Loss",
                    "SmoothL1Loss": "SmoothL1Loss",
                    "BCELoss": "BCELoss",
                }
            }
        },
        "LearningRate": {
            "learningRate": {
                "type": "float",
                "default": 0.001,
                "min": 0
            }
        },
        "OptimizerPara": {
            "SGD": {
                "momentum": {
                    "type": "float",
                    "default": 0.9,
                    "max": 1,
                    "min": 0
                },
                "dampening": {
                    "type": "float",
                    "default": 0,
                    "max": 1,
                    "min": 0
                },
                "weightDecay": {
                    "type": "float",
                    "default": 5e-4,
                    "max": 1,
                    "min": 0
                },
                "nesterov": {
                    "type": "boolean",
                    "default": False
                }
            },
            "Adam": {
                "betas": {
                    "children": {
                        "min": {
                            "type": "float",
                            "default": 0.9,
                            "max": 1,
                            "min": 0,
                        },
                        "max": {
                            "type": "float",
                            "default": 0.999,
                            "max": 1,
                            "min": 0,
                        },
                    }
                },
                "eps": {
                    "type": "float",
                    "default": 1e-8,
                    "max": 1,
                    "min": 0
                },
                "weightDecay": {
                    "type": "float",
                    "default": 0,
                    "max": 1,
                    "min": 0
                },
                "amsgrad": {
                    "type": "boolean",
                    "default": False
                }
            },
            "Adadelta": {
                "rho":  {
                    "type": "float",
                    "default": 0.9,
                    "max": 1,
                    "min": 0
                },
                "eps": {
                    "type": "float",
                    "default": 1e-6,
                    "max": 1,
                    "min": 0
                },
                "weightDecay": {
                    "type": "float",
                    "default": 0,
                    "max": 1,
                    "min": 0
                }
            },
            "AdamW": {
                "betas": {
                    "children": {
                        "min": {
                            "type": "float",
                            "default": 0.9,
                            "max": 1,
                            "min": 0,
                        },
                        "max": {
                            "type": "float",
                            "default": 0.999,
                            "max": 1,
                            "min": 0,
                        },
                    }
                },
                "eps": {
                    "type": "float",
                    "default": 1e-8,
                    "max": 1,
                    "min": 0
                },
                "weightDecay": {
                    "type": "float",
                    "default": 0.01,
                    "max": 1,
                    "min": 0
                },
                "amsgrad": {
                    "type": "boolean",
                    "default": False
                }
            },
            "NAdam": {
                "betas": {
                    "children": {
                        "min": {
                            "type": "float",
                            "default": 0.9,
                            "max": 1,
                            "min": 0,
                        },
                        "max": {
                            "type": "float",
                            "default": 0.999,
                            "max": 1,
                            "min": 0,
                        },
                    }
                },
                "eps": {
                    "type": "float",
                    "default": 1e-8,
                    "max": 1,
                    "min": 0
                },
                "weightDecay": {
                    "type": "float",
                    "default": 0.01,
                    "max": 1,
                    "min": 0
                },
                "momentumDecay": {
                    "type": "float",
                    "default": 0.004,
                    "max": 1,
                    "min": 0
                }
            }
        },
        "SchedulerPara": {
            "stepLR": {
                "stepSize": {
                    "type": "int",
                    "default": 10,
                    "min": 1
                },
                "gamma": {
                    "type": "float",
                    "default": 0.1
                }
            },
            "cosineAnnealingLR": {
                "tMax": {
                    "type": "int",
                    "min": 1
                },
                "etaMin": {
                    "type": "float",
                    "default": 0,
                    "min": 0
                }
            }
        }
    },
    "ConfigPreprocess": {
        "PreprocessPara": {
            "normalize": {
                "mode": {
                    "type": "int",
                    "default": 0,
                    "enums": {
                        "ImageNet": 0,
                        "CIFAR10": 1,
                        "MNIST": 2,
                        "CalculateFromData": 3,
                        "UserInput": 4
                    }
                },
                "mean": {
                    "children": {
                        "R": {
                            "type": "float",
                            "default": 0.5,
                            "min": 0,
                        },
                        "G": {
                            "type": "float",
                            "default": 0.5,
                            "min": 0,
                        },
                        "B": {
                            "type": "float",
                            "default": 0.5,
                            "min": 0,
                        },
                    },
                    "nullable": True
                },
                "std": {
                    "type": "list[float]",
                    "default": [0.5, 0.5, 0.5],
                    "min": 0,
                    "len": 3,
                    "nullable": True
                }
            },
            "resize": {
                "imageSize": {
                    "type": "list[int]",
                    "default": [224, 224],
                    "min": 1,
                    "len": 2
                },
                "interpolation": {
                    "type": "string",
                    "default": "BILINEAR",
                    "enums": {
                        "BILINEAR": "BILINEAR",
                        "NEAREST": "NEAREST",
                        "BICUBIC": "BICUBIC"
                    }
                }
            },
            "centerCrop": {
                "size": {
                    "type": "list[int]",
                    "default": [1, 1],
                    "min": 0,
                    "len": 2
                }
            },
            "pad": {
                "padding":  {
                    "type": "list[int]",
                    "default": [0, 0, 0, 0],
                    "min": 0,
                    "len": 4
                },
                "fill": {
                    "type": "list[int]",
                    "default": [0, 0, 0],
                    "max": 255,
                    "min": 0,
                    "len": 3,
                    "nullable": True
                },
                "paddingModel": {
                    "type": "string",
                    "default": "constant",
                    "enums": {
                        "constant": "constant",
                        "edge": "edge",
                        "reflect": "reflect",
                        "symmetric": "symmetric",
                    }
                }
            },
            "gaussianBlur": {
                "kernelSize":
                {
                    "type": "list[int]",
                    "default": [3, 3],
                    "min": 1,
                    "len": 2
                },
                "sigma": {
                    "type": "float",
                    "default": 0,
                    "min": 0
                }
            },
            "brightness": {
                "brightness": {
                    "type": "float",
                    "default": 1,
                    "min": 0
                }
            },
            "contrast": {
                "contrast": {
                    "type": "float",
                    "default": 1,
                    "min": 0
                }
            },
            "saturation": {
                "saturation": {
                    "type": "float",
                    "default": 1,
                    "min": 0
                }
            },
            "hue": {
                "hue": {
                    "type": "float",
                    "default": 0,
                    "max": 0.5,
                    "min": -0.5
                }
            }
        }
    },
    "ConfigPytorchModel": {
        "SelectedModel": {
            "model": {
                "structure": {
                    "type": "string",
                    "default": "auo_unrestricted_powerful_model",
                    "enums": {
                        "auo_tiny_focus_model": "auo_tiny_focus_model",
                        "auo_classic_deep_model": "auo_classic_deep_model",
                        "auo_anti_degeneration_mode": "auo_anti_degeneration_mode",
                        "auo_transform_aggregate_model": "auo_transform_aggregate_model",
                        "auo_narrow_intensive_model": "auo_narrow_intensive_model",
                        "auo_feature_enhance_model_a": "auo_feature_enhance_model_a",
                        "auo_feature_enhance_model_b": "auo_feature_enhance_model_b",
                        "auo_feature_enhance_model_c": "auo_feature_enhance_model_c",
                        "auo_faster_convergency_mode": "auo_faster_convergency_mode",
                        "auo_unrestricted_powerful_model": "auo_unrestricted_powerful_model",
                        "auo_feature_reuse_model": "auo_feature_reuse_model",
                        "auo_lighten_efficient_model": "auo_lighten_efficient_model",
                        "auo_horizontal_sample_model": "auo_horizontal_sample_model"
                    }
                },
                "pretrained": {
                    "type": "boolean",
                    "default": True
                }
            },
            "ClsModelPara": {
                "batchSize": {
                    "type": "int",
                    "default": 1,
                    "min": 1
                },
                "epochs": {
                    "type": "int",
                    "default": 1,
                    "min": 1
                }
            }
        },
        "ConfigResultStorage": {
            "ResultStorage": {
                "saveFinalWeight": {
                    "switch": {
                        "type": "boolean",
                        "default": False
                    }
                },
                "saveAccTxt": {
                    "switch": {
                        "type": "boolean",
                        "default": False
                    }
                },
                "savePredictResult": {
                    "switch": {
                        "type": "boolean",
                        "default": True
                    }
                },
                "unknownFilter": {
                    "switch": {
                        "type": "boolean",
                        "default": False
                    },
                    "filter": {
                        "type": "dict[str, float]",
                        "default": {"unknown": 0.5},
                        "max": 1,
                        "min": 0
                    },
                    "reverse": {
                        "type": "boolean",
                        "default": False
                    },
                    "saveCsv": {
                        "type": "int",
                        "default": 2,
                        "enums": {
                            "none": 0,
                            "filtered": 1,
                            "both": 2
                        }
                    }
                }
            }
        },
        "ConfigPass": {
            "confidenceFilter": False,
            "showRate": False,
            "cudaDevice": 0,
            "saveAccJson": True,
            "testAccJson": True,
            "drawAccCurve": False,
            "drawConfusionMatrix": True
        }
    }
}
