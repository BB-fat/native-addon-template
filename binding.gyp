{
  "targets": [
    {
      "target_name": "bindings",
      "sources": [
        "src/export.cc"
      ],
      "include_dirs": [
        "<!@(node -p \"require('node-addon-api').include\")"
      ],
      "dependencies": [
        "<!(node -p \"require('node-addon-api').gyp\")"
      ],
      "cflags!": ["-fno-exceptions"],
      "cflags_cc!": ["-fno-exceptions"],
      "defines": [
        "NAPI_CPP_EXCEPTIONS",
        "NAPI_VERSION=3",
      ],
      "conditions": [
        [
          'OS=="mac"',
          {
            "sources": [
                'src/add.mm'
            ],
            'link_settings': {
              'libraries': [
                '-framework CoreFoundation',
                '-framework AppKit',
              ]
            },
            "xcode_settings": {
              "GCC_ENABLE_CPP_EXCEPTIONS": "YES",
              "CLANG_ENABLE_OBJC_ARC": "YES",
              'OTHER_CFLAGS': [
                '-ObjC++',
                '-std=c++17'
              ]
            },
          }
        ],
#         [
#           'OS=="win"',
#           {
#             "sources": [
#             ],
#             "libraries": [
#             ],
#             "msvs_settings": {
#               "VCCLCompilerTool": {
#                 "AdditionalOptions": ["/std:c++17"]
#               }
#             },
#           }
#         ],
      ]
    }
  ]
}
