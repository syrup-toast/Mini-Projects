ask = input("Farenheit or Celcius? ")
if ask == "C":
    Cresponse = int(input("What tempature is it?(Farenheit)."))
    C = (Cresponse - 32) * 5/9
    print("So if it's " + str(Cresponse) + " in Farenheit, it should be " + str(C) + " in Celcius.")
elif ask == "F":
    response = int(input("What tempature is it?(celcius)")) # asks what tempature it is, waiting for a response.
    F = response * 1.8 + 32
    print ("so if it's " + str(response) + " in celcius it should be " + str(F) + " in Farenheit.")
