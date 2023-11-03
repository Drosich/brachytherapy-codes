import gantry


def main():
	
	g = gantry.Gantry('/dev/ttyUSB0')
	g.disconnect()

if __name__ == '__main__':
	main()
