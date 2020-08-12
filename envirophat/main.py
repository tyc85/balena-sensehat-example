#!/usr/bin/python
from flask import Flask, jsonify
#https://learn.pimoroni.com/tutorial/sandyj/getting-started-with-enviro-phat
#http://docs.pimoroni.com/envirophat/
#https://github.com/pimoroni/enviro-phat
from envirophat import light, weather, motion, analog, leds

app = Flask(__name__)

@app.route('/')
def api_Description():
    return '''
<!DOCTYPE html><html><head><title>Envirophat Environmental Data API</title></head>
<body><h1>Envirophat Environmental Data API</h1>
<p>A REST API for getting Envirophat environmental data.</p>
<p>Usage: https://URL/api/COMMAND_CATEGORY/COMMAND/OPTIONS_LIST
<ul>
	<li>light</li>
		<ul>
			<li>light</li>
			<li>max_count</b></li>
			<li>raw</li>
			<li>rgb</li>
			<li>scaled</li>
			<li>set_integration_time_ms</li>
				<ul>
					<li>ms - The integration time in milliseconds from 2.4 to 612, in increments of 2.4. Default = 511.2</li>
				</ul>
		</ul>
	<li>motion</li>
		<ul>
			<li>accelerometer</li>
			<li>heading</li>
			<li>is_mag_ready</li>
			<li>magnetometer</li>
			<li>raw_heading</li>
		</ul>
	<li>weather</li>
		<ul>
			<li>altitude</li>
				<ul>
					<li>qnh. default = 1013.25 (hpA)</li>
				</ul>
			<li>pressure</li>
				<ul>
					<li>hPa (hectopascals)</li>
					<li>Pa (pascals)</li>
				</ul>
			<li>temperature</li>
			<li>update</li>
		</ul>
	<li>analog</li>
		<ul>
			<li>available</li>
			<li>read_all</li>
			<li>read</li>
				<ul>
					<li>channel - 0 to 3. Default = 0</li>
					<li>programmable_gain - 6144, 4096, 2048, 1024, 512, 256 (default 4096 or 6144 depending on revision). Library default = None</li>
					<li>samples_per_second - 128, 250, 498, 920, 1600, 2400, 3300 (default 1600)</li>
				</ul>
		</ul>
	<li>leds</li>
		<ul>
			<li>is_on</li>
			<li>is_off</li>
			<li>on</li>
			<li>off</li>
		</ul>
</ul></p></body></html>
'''

def convert_accelerometer():
    return list(motion.accelerometer())

def convert_magnetometer():
    return list(motion.magnetometer())

@app.route('/api/weather/altitude/<qnh>', methods=['GET'])
def api_command_qnh(qnh):
    #qnh=1020
    print(qnh)
    data = weather.altitude(qnh=float(qnh))
    print(data)
    return jsonify(data)

@app.route('/api/weather/pressure/<unit>', methods=['GET'])
def api_command_pressure_units(unit):
    #hPa (hectopascals)
    #Pa (pascals)
    print(unit)
    data = weather.pressure(unit=str(unit))
    print(data)
    return jsonify(data)

@app.route('/api/light/set_integration_time_ms/<ms>', methods=['GET'])
def api_command_light_set_integration_time(ms):
    #ms - The integration time in milliseconds from 2.4 to 612, in increments of 2.4.
    #setup sets set_integration_time_ms to 511.2
    data = light.set_integration_time_ms(float(ms))
    return jsonify(data)

@app.route('/api/analog/read/<channel>/<programmable_gain>/<samples_per_second>', methods=['GET'])
def api_command_analog_read(channel, programmable_gain, samples_per_second):
    #analog.read(channel=0, programmable_gain=None, samples_per_second=1600)
    #channel - 0 to 3
    #programmable_gain - 6144, 4096, 2048, 1024, 512, 256 (default 4096 or 6144 depending on revision)
    #samples_per_second - 128, 250, 498, 920, 1600, 2400, 3300 (default 1600)
    data = analog.read(channel=int(channel), programmable_gain=int(programmable_gain), samples_per_second=int(samples_per_second))
    return jsonify(data)  

@app.route('/api/<command_category>/<command>', methods=['GET'])
def api_commands(command_category, command):
    command_dict = {'light': {'light': light.light, 'max_count': light.max_count, 'raw': light.raw, 'rgb': light.rgb, 'scaled': light.scaled},
		    'motion': {'accelerometer': convert_accelerometer, 'heading': motion.heading, 'is_mag_ready': motion.is_mag_ready, \
		    'magnetometer':convert_magnetometer , 'raw_heading': motion.raw_heading},
		    'weather': {'altitude': weather.altitude, 'pressure': weather.pressure, 'temperature': weather.temperature, 'update': weather.update},
                    'analog': {'available': analog.available, 'read_all': analog.read_all, 'read': analog.read},
                    'leds': {'is_on': leds.is_on, 'is_off': leds.is_off, 'on': leds.on, 'off': leds.off}
        }
    print(command_category + ":" + command)
    data = command_dict[command_category][command]()
    print(data)
    print(type(data))
    return jsonify(data)


if __name__ == '__main__':
    app.run(host='0.0.0.0', port=80)

