
from collections.abc import Sequence, Any


def cut_end(string: str, ending: str) -> str:
	if string.endswith(ending):
		return string[:-len(ending)]
	return string

def ensure_endswith(string: str, suffix: str) -> str:
	if not string.endswith(suffix):
		return string + suffix
	return string

def getitem[T, D](l: Sequence[T], index: int, default: D=None) -> T | D:
	return l[index] if -len(l) <= index < len(l) else default

def isdigit(s: Any) -> bool:
	try:
		int(s)
		return True
	except (ValueError, TypeError):
		return False

