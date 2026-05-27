"""Generated from Smithy shape ``com.amazonaws.dynamodb#GetResourcePolicy``."""

from __future__ import annotations
from typing import TYPE_CHECKING
import zapros
import aws_sdk_dynamodb._auth._signers
from aws_sdk_dynamodb._services._pipeline import AsyncOperationOptions, OperationOptions

if TYPE_CHECKING:
    import aws_sdk_dynamodb.types.get_resource_policy_input
    import aws_sdk_dynamodb.types.get_resource_policy_output


def get_resource_policy(
    options: OperationOptions,
    input: aws_sdk_dynamodb.types.get_resource_policy_input.GetResourcePolicyInput,
) -> tuple[
    aws_sdk_dynamodb.types.get_resource_policy_output.GetResourcePolicyOutput,
    zapros.Response,
]:
    raise NotImplementedError("operation dispatch not yet generated")


async def async_get_resource_policy(
    options: AsyncOperationOptions,
    input: aws_sdk_dynamodb.types.get_resource_policy_input.GetResourcePolicyInput,
) -> tuple[
    aws_sdk_dynamodb.types.get_resource_policy_output.GetResourcePolicyOutput,
    zapros.Response,
]:
    raise NotImplementedError("operation dispatch not yet generated")
