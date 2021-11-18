// Copyright 2021 alexju
#include <napi.h>
#include <tuple>
#include "add.h"

Napi::Number AddJs(const Napi::CallbackInfo &info) {
    Napi::Env env = info.Env();
    if (info.Length() != 2) {
        Napi::TypeError::New(env, "Expect 2 arguments.")
                .ThrowAsJavaScriptException();
        return Napi::Number::New(env, 0);
    }
    int result = add(info[0].As<Napi::Number>(), info[1].As<Napi::Number>());
    return Napi::Number::New(env, result);
}

Napi::Object Init(Napi::Env env, Napi::Object exports) {
    exports.Set("add", Napi::Function::New(env, AddJs));
    return exports;
}

NODE_API_MODULE(add, Init)