"""Generated from Smithy shape ``com.amazonaws.secretsmanager#DeleteResourcePolicy``."""

from __future__ import annotations
from typing import TYPE_CHECKING
import zapros
import aws_sdk_secrets_manager._auth._signers
from aws_sdk_secrets_manager._services._pipeline import (
    AsyncOperationOptions,
    OperationOptions,
)

if TYPE_CHECKING:
    import aws_sdk_secrets_manager.types.delete_resource_policy_request
    import aws_sdk_secrets_manager.types.delete_resource_policy_response


def delete_resource_policy(
    options: OperationOptions,
    input: aws_sdk_secrets_manager.types.delete_resource_policy_request.DeleteResourcePolicyRequest,
) -> tuple[
    aws_sdk_secrets_manager.types.delete_resource_policy_response.DeleteResourcePolicyResponse,
    zapros.Response,
]:
    raise NotImplementedError("operation dispatch not yet generated")


async def async_delete_resource_policy(
    options: AsyncOperationOptions,
    input: aws_sdk_secrets_manager.types.delete_resource_policy_request.DeleteResourcePolicyRequest,
) -> tuple[
    aws_sdk_secrets_manager.types.delete_resource_policy_response.DeleteResourcePolicyResponse,
    zapros.Response,
]:
    raise NotImplementedError("operation dispatch not yet generated")
