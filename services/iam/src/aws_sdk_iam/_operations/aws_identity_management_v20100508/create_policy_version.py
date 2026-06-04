"""Generated from Smithy shape ``com.amazonaws.iam#CreatePolicyVersion``."""

from __future__ import annotations
from typing import TYPE_CHECKING
import zapros
import aws_sdk_iam._auth._signers
from aws_sdk_iam._services._pipeline import AsyncOperationOptions, OperationOptions

if TYPE_CHECKING:
    import aws_sdk_iam.types.create_policy_version_request
    import aws_sdk_iam.types.create_policy_version_response


def create_policy_version(
    options: OperationOptions,
    input: aws_sdk_iam.types.create_policy_version_request.CreatePolicyVersionRequest,
) -> tuple[
    aws_sdk_iam.types.create_policy_version_response.CreatePolicyVersionResponse,
    zapros.Response,
]:
    raise NotImplementedError("operation dispatch not yet generated")


async def async_create_policy_version(
    options: AsyncOperationOptions,
    input: aws_sdk_iam.types.create_policy_version_request.CreatePolicyVersionRequest,
) -> tuple[
    aws_sdk_iam.types.create_policy_version_response.CreatePolicyVersionResponse,
    zapros.Response,
]:
    raise NotImplementedError("operation dispatch not yet generated")
