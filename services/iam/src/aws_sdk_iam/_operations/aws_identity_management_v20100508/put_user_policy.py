"""Generated from Smithy shape ``com.amazonaws.iam#PutUserPolicy``."""

from __future__ import annotations
from typing import TYPE_CHECKING
import zapros
import aws_sdk_iam._auth._signers
from aws_sdk_iam._services._pipeline import AsyncOperationOptions, OperationOptions

if TYPE_CHECKING:
    import aws_sdk_iam.types.put_user_policy_request


def put_user_policy(
    options: OperationOptions,
    input: aws_sdk_iam.types.put_user_policy_request.PutUserPolicyRequest,
) -> tuple[None, zapros.Response]:
    raise NotImplementedError("operation dispatch not yet generated")


async def async_put_user_policy(
    options: AsyncOperationOptions,
    input: aws_sdk_iam.types.put_user_policy_request.PutUserPolicyRequest,
) -> tuple[None, zapros.Response]:
    raise NotImplementedError("operation dispatch not yet generated")
