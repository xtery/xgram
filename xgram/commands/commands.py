__commands = dict()
		
def create(name):
	def callable(fn):
		__create(name, fn)
		return fn
	return callable
	
def __create(name, fn):
	
	if isinstance(name, list):
		for n in name:
			__create(n, fn)
		return
	elif not isinstance(name, str):
		raise CommandNameException('Command name must be str or list')
	
	if __commands.get(name) != None:
		raise DuplicateCommandException(name)
		
	__commands[name] = fn
	pass

def get(name):
	return __commands.get(name)
