import abc
import uuid
import logging
import typing


L = logging.getLogger(__name__)

class ToolProviderABC(abc.ABC):

	def __init__(self, tool_service):
		self.ToolService = tool_service
		self.Id = str(uuid.uuid4())

	@abc.abstractmethod
	async def initialize(self):
		pass

	@abc.abstractmethod
	async def execute(self, function_call) -> typing.AsyncGenerator[typing.Any, None]:
		pass
	