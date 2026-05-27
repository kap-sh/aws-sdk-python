"""Generated from Smithy shape ``com.amazonaws.ecs#ListTaskDefinitionFamilies``."""

from __future__ import annotations
from typing import TYPE_CHECKING
import zapros
import aws_sdk_ecs._auth._signers
from aws_sdk_ecs._services._pipeline import AsyncOperationOptions, OperationOptions

if TYPE_CHECKING:
    import aws_sdk_ecs.types.list_task_definition_families_request
    import aws_sdk_ecs.types.list_task_definition_families_response


def list_task_definition_families(
    options: OperationOptions,
    input: aws_sdk_ecs.types.list_task_definition_families_request.ListTaskDefinitionFamiliesRequest,
) -> tuple[
    aws_sdk_ecs.types.list_task_definition_families_response.ListTaskDefinitionFamiliesResponse,
    zapros.Response,
]:
    raise NotImplementedError("operation dispatch not yet generated")


async def async_list_task_definition_families(
    options: AsyncOperationOptions,
    input: aws_sdk_ecs.types.list_task_definition_families_request.ListTaskDefinitionFamiliesRequest,
) -> tuple[
    aws_sdk_ecs.types.list_task_definition_families_response.ListTaskDefinitionFamiliesResponse,
    zapros.Response,
]:
    raise NotImplementedError("operation dispatch not yet generated")
