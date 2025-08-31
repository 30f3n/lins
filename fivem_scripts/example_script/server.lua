local LICENSE_KEY = "ضع_الرخصة_هنا"

PerformHttpRequest("http://127.0.0.1:5000/verify", function(statusCode, response, headers)
    if statusCode ~= 200 then
        print("الرخصة غير صالحة! السكربت لن يعمل.")
        return
    end
    print("تم التحقق من الرخصة، السكربت يعمل الآن.")

    -- هنا ضع باقي كود السكربت الخاص بك
    RegisterCommand("hello", function(source, args, rawCommand)
        print("مرحباً بك في السكربت!")
    end, false)

end, "POST", json.encode({license_key = LICENSE_KEY}), {["Content-Type"] = "application/json"})
