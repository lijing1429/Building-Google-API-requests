# Build Google API requests

The aim of this project is creating the request URLs according to the [google API documents](https://developers.google.com/maps/documentation/directions/get-directions).

## Introduction

- **Input parameters**: 

| Parameters | Description |
| ----------- | ----------- |
| Origin address | Reuired. Any UK postcode. |
| Destination address | Reuired. Any UK postcode. |
| Driving mode | Optional. *Y* or *N* |
| Searching time | Optional. Any future time. |

- **Output data**: Google API json data

- **Tools**:  python, Google API Direction

- **Main task**:  convert the input data into the URL, then output a json result data.

## Difficulties

**Covert time to different format**: input time may have different format, you should consider every possibility in your codes

## Future improvement 

- **Add more paraments**: avoid, transit_mode, transit_routing_preference etc.
  
- **Change the address**: change to longitude and latitude could be faster than this version.

## How to use?

You can just copy the **example.py** and put your **Google API key** into the codes, then you can get the request result data.
