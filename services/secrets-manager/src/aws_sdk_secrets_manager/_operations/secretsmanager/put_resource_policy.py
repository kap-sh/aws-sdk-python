"""Generated from Smithy shape ``com.amazonaws.secretsmanager#PutResourcePolicy``."""

from __future__ import annotations
from typing import TYPE_CHECKING
import zapros
import aws_sdk_secrets_manager._auth._signers
from aws_sdk_secrets_manager._services._pipeline import (
    AsyncOperationOptions,
    OperationOptions,
)

if TYPE_CHECKING:
    import aws_sdk_secrets_manager.types.put_resource_policy_request
    import aws_sdk_secrets_manager.types.put_resource_policy_response


def put_resource_policy(
    options: OperationOptions,
    input: aws_sdk_secrets_manager.types.put_resource_policy_request.PutResourcePolicyRequest,
) -> tuple[
    aws_sdk_secrets_manager.types.put_resource_policy_response.PutResourcePolicyResponse,
    zapros.Response,
]:
    raise NotImplementedError("operation dispatch not yet generated")


async def async_put_resource_policy(
    options: AsyncOperationOptions,
    input: aws_sdk_secrets_manager.types.put_resource_policy_request.PutResourcePolicyRequest,
) -> tuple[
    aws_sdk_secrets_manager.types.put_resource_policy_response.PutResourcePolicyResponse,
    zapros.Response,
]:
    raise NotImplementedError("operation dispatch not yet generated")
