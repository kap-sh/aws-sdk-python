"""Generated from Smithy shape ``com.amazonaws.ecs#UpdateContainerAgent``."""

from __future__ import annotations
from typing import TYPE_CHECKING
import zapros
import aws_sdk_ecs._auth._signers
from aws_sdk_ecs._services._pipeline import AsyncOperationOptions, OperationOptions

if TYPE_CHECKING:
    import aws_sdk_ecs.types.update_container_agent_request
    import aws_sdk_ecs.types.update_container_agent_response


def update_container_agent(
    options: OperationOptions,
    input: aws_sdk_ecs.types.update_container_agent_request.UpdateContainerAgentRequest,
) -> tuple[
    aws_sdk_ecs.types.update_container_agent_response.UpdateContainerAgentResponse,
    zapros.Response,
]:
    raise NotImplementedError("operation dispatch not yet generated")


async def async_update_container_agent(
    options: AsyncOperationOptions,
    input: aws_sdk_ecs.types.update_container_agent_request.UpdateContainerAgentRequest,
) -> tuple[
    aws_sdk_ecs.types.update_container_agent_response.UpdateContainerAgentResponse,
    zapros.Response,
]:
    raise NotImplementedError("operation dispatch not yet generated")
