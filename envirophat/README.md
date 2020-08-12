# Environmental Data Server

**Environmental Data Server API**

https://a9607eaac2d419c42c3087f37d6261dc.balena-devices.com

**Envirophat library**

https://github.com/pimoroni/enviro-phat

**Usage:**

 https://URL/api/COMMAND_CATEGORY/COMMAND/OPTIONS_LIST

**Commands:**
 
- COMMAND_CATEGORY
	- COMMAND
		- OPTIONS_LIST
 
- light
	- light
	- max_count
	- raw
	- rgb
	- scaled
	- set_integration_time_ms
		- ms -- The integration time in milliseconds from 2.4 to 612, in increments of 2.4. Default = 511.2
- motion
	- accelerometer
	- heading
	- is_mag_ready
	- magnetometer
	- raw_heading
- weather
	- altitude
		- qnh -- default = 1013.25 (hpA)
	- pressure
		- hPa (hectopascals)
		- Pa (pascals)
	- temperature
	- update
- analog
	- available
	- read_all
	- read
		- channel -- 0 to 3. Default = 0
		- programmable_gain -- 6144, 4096, 2048, 1024, 512, 256 (default 4096 or 6144 depending on revision). Library default = None
		- samples_per_second - 128, 250, 498, 920, 1600, 2400, 3300 (default 1600)
- leds
	- is_on
	- is_off
	- on
	- off
	
**Examples:**
```
https://a9607eaac2d419c42c3087f37d6261dc.balena-devices.com/api/light/light
2668
```
```
https://a9607eaac2d419c42c3087f37d6261dc.balena-devices.com/api/light/max_count
44032
```
```
https://a9607eaac2d419c42c3087f37d6261dc.balena-devices.com/api/light/raw
[829,887,572,2394]
```
```
https://a9607eaac2d419c42c3087f37d6261dc.balena-devices.com/api/light/rgb
[88,94,61]
```
```
https://a9607eaac2d419c42c3087f37d6261dc.balena-devices.com/api/light/scaled
[0.3435655253837072,0.371900826446281,0.24124360487996852,1.0]
```
```
https://a9607eaac2d419c42c3087f37d6261dc.balena-devices.com/api/light/set_integration_time_ms/511.2
null
```
```
https://a9607eaac2d419c42c3087f37d6261dc.balena-devices.com/api/motion/accelerometer
[-0.03143310546875,0.1229248046875,1.050048828125]
```
```
https://a9607eaac2d419c42c3087f37d6261dc.balena-devices.com/api/motion/heading
22.79
```
```
https://a9607eaac2d419c42c3087f37d6261dc.balena-devices.com/api/motion/is_mag_ready
true
```
```
https://a9607eaac2d419c42c3087f37d6261dc.balena-devices.com/api/motion/magnetometer
[2883,424,-4862]
```
```
https://a9607eaac2d419c42c3087f37d6261dc.balena-devices.com/api/motion/raw_heading
81.63
```
```
https://a9607eaac2d419c42c3087f37d6261dc.balena-devices.com/api/weather/altitude
313.03711222865974
```
```
https://a9607eaac2d419c42c3087f37d6261dc.balena-devices.com/api/weather/altitude/1013.25
313.79741360291445
```
```
https://a9607eaac2d419c42c3087f37d6261dc.balena-devices.com/api/weather/pressure
97613.53768764964
```
```
https://a9607eaac2d419c42c3087f37d6261dc.balena-devices.com/api/weather/pressure/hPa
976.1246962564127
```
```
https://a9607eaac2d419c42c3087f37d6261dc.balena-devices.com/api/weather/pressure/Pa
97611.22645926152
```
```
https://a9607eaac2d419c42c3087f37d6261dc.balena-devices.com/api/weather/temperature
30.71090131153253
```
```
https://a9607eaac2d419c42c3087f37d6261dc.balena-devices.com/api/weather/update
null
```
```
https://a9607eaac2d419c42c3087f37d6261dc.balena-devices.com/api/analog/available
true
```
```
https://a9607eaac2d419c42c3087f37d6261dc.balena-devices.com/api/analog/read_all
[0.531,0.54,0.546,0.534]
```
```
https://a9607eaac2d419c42c3087f37d6261dc.balena-devices.com/api/analog/read
0.516
```
```
https://a9607eaac2d419c42c3087f37d6261dc.balena-devices.com/api/analog/read/0/4096/1600
0.542
```
```
https://a9607eaac2d419c42c3087f37d6261dc.balena-devices.com/api/leds/is_on
false
```
```
https://a9607eaac2d419c42c3087f37d6261dc.balena-devices.com/api/leds/is_off
true
```
```
https://a9607eaac2d419c42c3087f37d6261dc.balena-devices.com/api/leds/on
true
```
```
https://a9607eaac2d419c42c3087f37d6261dc.balena-devices.com/api/leds/off
null
```
