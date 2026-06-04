"""Generated from Smithy shape ``com.amazonaws.iam#DetachUserPolicy``."""

from __future__ import annotations
from typing import TYPE_CHECKING
import zapros
import aws_sdk_iam._auth._signers
from aws_sdk_iam._services._pipeline import AsyncOperationOptions, OperationOptions

if TYPE_CHECKING:
    import aws_sdk_iam.types.detach_user_policy_request


def detach_user_policy(
    options: OperationOptions,
    input: aws_sdk_iam.types.detach_user_policy_request.DetachUserPolicyRequest,
) -> tuple[None, zapros.Response]:
    raise NotImplementedError("operation dispatch not yet generated")


async def async_detach_user_policy(
    options: AsyncOperationOptions,
    input: aws_sdk_iam.types.detach_user_policy_request.DetachUserPolicyRequest,
) -> tuple[None, zapros.Response]:
    raise NotImplementedError("operation dispatch not yet generated")
