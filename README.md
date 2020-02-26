# Overview
In Oxford, most bus stops have a screen that shows what buses will stop here and how soon they will do so.
This data is available on the website www.oxontime.com, but there is no official API for accessing this data.

Oxontime gets its live data from www.buscms.com, and this Python script pulls from this source and outputs the bustimes as a list.

## Background
I built this because I was surprised that nobody else had built a simple script that solely returned data from OxonTime in a usable format.
Please use this in your own projects! I'd like to see what you do with it!

# Inputs

The only required input is the bus stop code. This can be found at all of the bus stops, but fortunately it can also be found on Oxontime on [this page](http://www.oxontime.com/livetimes.shtml?q=) where you can search by name/location.

# Example

## Code

``` 
from oxonTime import getBusTimes

magdalenStreet = '69326546'

print(getBusess(magdalenStreet))
```

## Output

``` 
[
    {'Service': '2', 'Destination': 'Kidlington', 'eta': '1 mins'},
    {'Service': '2A', 'Destination': 'Kidlington', 'eta': '11 mins'},
    {'Service': '2B', 'Destination': 'Kidlington', 'eta': '23 mins'},
    {'Service': '2', 'Destination': 'Kidlington', 'eta': '31 mins'},
    {'Service': '2A', 'Destination': 'Kidlington', 'eta': '41 mins'}
]
```

