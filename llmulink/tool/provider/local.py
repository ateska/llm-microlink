import logging
import typing

from .provider_abc import ToolProviderABC
from .local_tools.ping import tool_ping
from ..tool import FunctionCallTool

#

L = logging.getLogger(__name__)

#
class LocalToolProvider(ToolProviderABC):
		

	async def initialize(self):
		tools = [
			FunctionCallTool(
				name = "ping",
				title = "Ping a host",
				description = "Ping a host and return the result",
				parameters = {
					"type": "object",
					"properties": {
						"host": {
							"type": "string",
							"description": "The host to ping"
						}
					},
					"required": ["host"]
				}
			)
		]
		self.ToolService._register(self, tools)


	async def execute(self, function_call) -> typing.AsyncGenerator[typing.Any, None]:
		match function_call.name:
			case "ping":
				async for _ in tool_ping(function_call):
					yield _
			case _:
				function_call.error = "Tool not found"
				function_call.error = True
				yield
