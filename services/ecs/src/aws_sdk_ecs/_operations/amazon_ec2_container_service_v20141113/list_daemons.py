"""Generated from Smithy shape ``com.amazonaws.ecs#ListDaemons``."""

from __future__ import annotations
from typing import TYPE_CHECKING
import zapros
import aws_sdk_ecs._auth._signers
from aws_sdk_ecs._services._pipeline import AsyncOperationOptions, OperationOptions

if TYPE_CHECKING:
    import aws_sdk_ecs.types.list_daemons_request
    import aws_sdk_ecs.types.list_daemons_response


def list_daemons(
    options: OperationOptions,
    input: aws_sdk_ecs.types.list_daemons_request.ListDaemonsRequest,
) -> tuple[
    aws_sdk_ecs.types.list_daemons_response.ListDaemonsResponse, zapros.Response
]:
    raise NotImplementedError("operation dispatch not yet generated")


async def async_list_daemons(
    options: AsyncOperationOptions,
    input: aws_sdk_ecs.types.list_daemons_request.ListDaemonsRequest,
) -> tuple[
    aws_sdk_ecs.types.list_daemons_response.ListDaemonsResponse, zapros.Response
]:
    raise NotImplementedError("operation dispatch not yet generated")
