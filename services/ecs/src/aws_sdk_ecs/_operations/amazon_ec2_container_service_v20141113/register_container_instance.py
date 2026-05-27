"""Generated from Smithy shape ``com.amazonaws.ecs#RegisterContainerInstance``."""

from __future__ import annotations
from typing import TYPE_CHECKING
import zapros
import aws_sdk_ecs._auth._signers
from aws_sdk_ecs._services._pipeline import AsyncOperationOptions, OperationOptions

if TYPE_CHECKING:
    import aws_sdk_ecs.types.register_container_instance_request
    import aws_sdk_ecs.types.register_container_instance_response


def register_container_instance(
    options: OperationOptions,
    input: aws_sdk_ecs.types.register_container_instance_request.RegisterContainerInstanceRequest,
) -> tuple[
    aws_sdk_ecs.types.register_container_instance_response.RegisterContainerInstanceResponse,
    zapros.Response,
]:
    raise NotImplementedError("operation dispatch not yet generated")


async def async_register_container_instance(
    options: AsyncOperationOptions,
    input: aws_sdk_ecs.types.register_container_instance_request.RegisterContainerInstanceRequest,
) -> tuple[
    aws_sdk_ecs.types.register_container_instance_response.RegisterContainerInstanceResponse,
    zapros.Response,
]:
    raise NotImplementedError("operation dispatch not yet generated")
