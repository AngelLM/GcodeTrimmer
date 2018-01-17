# GcodeTrimmer

Sometimes when 3D printing the printer might run out of filament, it might break or get stuck. Then you have 2 options: to try to resume the print where it failed or restart it from scratch.

This script allows you to trim the Gcode easily at the height of your choice. It has been tested with a GCode made by Cura and it worked (example files are available in the "examples" folder).

Feel free to adapt it to your needs and share the modifications!

## How to resume a failed print.

Note: depending on the level of failure some prints couldn't be resumed properly.

1. Scrape the surface of your print until you get a flat surface (that should be the last well printed layer)
2. Measure the height of the print (the use of a caliper is suggested)
3. Open the gcode file of the failed print in the PC (text editor/notepad can do the work)
4. Find the closer Z height to your measure and remember it. (You can use the find tool to search "Z")
5. Execute the script using the Z height found in the previous step
6. Print the generated Gcode
7. Cross your fingers


## How to use the script

1. Clone the repository (or just download the python script).
2. Open the terminal and navigate to the folder where the script is.
3. Execute the script using python passing 3 additional arguments (Z coordinate, path to original gcode file, path to the new generated gcode file)

For example:
```
python GcodeTrimmer.py 14.200 examples/original.gcode examples/destination.gcode
```

Executing the script in this way, will generate a new file (destination.gcode) in the examples folder that will be the original file (original.gcode) trimmed at Z14.200


## License

<img src="By-sa.png" width="200">

All files included in this repository are licensed under a [Creative Commons Attribution-ShareAlike 4.0 International License](http://creativecommons.org/licenses/by-sa/4.0/)
