class CommandNameException(Exception):
	def __init__(self, message):
		super(CommandNameException, self).__init__(message)
		
class DuplicateCommandException(Exception):
	def __init__(self, cmd):
		super(DuplicateCommandException, self).__init__('A command('+ cmd +') can only be bound to one function.')
