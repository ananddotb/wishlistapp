class _MapIterator :
	def __init__(self, entrylist) :
		self._entryList = entrylist
		self._curEntry = 0
	
	def __iter__(self) :
		return self
	
	def __next__(self) :
		if self._curEntry < len(self._entryList) :
			entry = self._entryList[self._curEntry]
			self._curEntry += 1
			return entry
		else :
			raise StopIteration
	
	
	
	