"""Generated from Smithy shape ``com.amazonaws.iam#GetPolicy``."""

from __future__ import annotations
from typing import TYPE_CHECKING
import zapros
import aws_sdk_iam._auth._signers
from aws_sdk_iam._services._pipeline import AsyncOperationOptions, OperationOptions

if TYPE_CHECKING:
    import aws_sdk_iam.types.get_policy_request
    import aws_sdk_iam.types.get_policy_response


def get_policy(
    options: OperationOptions,
    input: aws_sdk_iam.types.get_policy_request.GetPolicyRequest,
) -> tuple[aws_sdk_iam.types.get_policy_response.GetPolicyResponse, zapros.Response]:
    raise NotImplementedError("operation dispatch not yet generated")


async def async_get_policy(
    options: AsyncOperationOptions,
    input: aws_sdk_iam.types.get_policy_request.GetPolicyRequest,
) -> tuple[aws_sdk_iam.types.get_policy_response.GetPolicyResponse, zapros.Response]:
    raise NotImplementedError("operation dispatch not yet generated")
