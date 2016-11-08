import sys,bfc,pymod
headers = ["# BF2P - Brainfuck to Python","# Made by MineRobber9000"]

if len(sys.argv) != 2:
	print("Usage: "+sys.argv[0]+" <file>")
	exit(-1)
else:
	global _filename
	_filename = sys.argv[1]

code = ""

with open(_filename) as f:
	for line in f:
		code += line + "\n"

code = bfc.clean(code)
mod = pymod.Program()

mod.addImport("print_function",True)
mod.addImport("sys",False)
mod.addLine("dp = 0")
mod.addLine("mem = {}")

charDict = {
	">": ["dp += 1"],
	"<": ["dp -= 1"],
	"+": ["if not dp in mem:","\tmem[dp] = 0","mem[dp] += 1"],
	"-": ["if not dp in mem:","\tmem[dp] = 0","mem[dp] -= 1"],
	"[": ["while mem[dp] != 0:"],
	"]": [], #nothing needs to be done here.
	",": ["if not dp in mem:","\tmem[dp] = 0","mem[dp] = ord(raw_input()[0])"],
	".": ["if not dp in mem:","\tmem[dp] = 0","print(chr(mem[dp]),end='')"]
}

indented = 0
for char in code:
#	if char == "[":
#		indented += 1
	if char == "]":
		indented -= 1
	for line in charDict[char]:
		mod.addLine(("\t"*indented)+line)
	if char == "[":
		indented += 1
mod.addLine("print()")

print(mod.fullcode(headers))
