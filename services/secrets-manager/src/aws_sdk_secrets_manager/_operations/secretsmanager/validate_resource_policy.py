"""Generated from Smithy shape ``com.amazonaws.secretsmanager#ValidateResourcePolicy``."""

from __future__ import annotations
from typing import TYPE_CHECKING
import zapros
import aws_sdk_secrets_manager._auth._signers
from aws_sdk_secrets_manager._services._pipeline import (
    AsyncOperationOptions,
    OperationOptions,
)

if TYPE_CHECKING:
    import aws_sdk_secrets_manager.types.validate_resource_policy_request
    import aws_sdk_secrets_manager.types.validate_resource_policy_response


def validate_resource_policy(
    options: OperationOptions,
    input: aws_sdk_secrets_manager.types.validate_resource_policy_request.ValidateResourcePolicyRequest,
) -> tuple[
    aws_sdk_secrets_manager.types.validate_resource_policy_response.ValidateResourcePolicyResponse,
    zapros.Response,
]:
    raise NotImplementedError("operation dispatch not yet generated")


async def async_validate_resource_policy(
    options: AsyncOperationOptions,
    input: aws_sdk_secrets_manager.types.validate_resource_policy_request.ValidateResourcePolicyRequest,
) -> tuple[
    aws_sdk_secrets_manager.types.validate_resource_policy_response.ValidateResourcePolicyResponse,
    zapros.Response,
]:
    raise NotImplementedError("operation dispatch not yet generated")
