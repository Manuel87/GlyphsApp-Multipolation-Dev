Syntax Example for a font with a flexible shadow axis (@RobertPraley)
```json
"Master Relations": {
        "Regular": {
            "Bold":{},
            "Light":{},
            "Shadow": {
                "ShadowAngle": {}
            }
        }
    },
    "Master Mapping": {
        "Regular":              [0,1],
            "Bold":             [85,160],
            "Light":            [85,20],
            "Shadow":           [0,1],
                "ShadowAngle":  [45,-45]
    },
    "Axes": {
        "WeightAxes": [["Light", "Regular", "Bold"], [20, 160]]
    },

    "InstancesSetup": {
        "VariableFont": {
            "Slider": {
                "Weight":       [[1, 220], "WeightAxes"],
                "Shadow":       [0, 1],
                "ShadowAngle":  [-45, 45]
            },
            "Master": {
                "Shadow":       "SliderShadow * SliderWeight"
            }
        }
    },
```
