"""Generated from Smithy shape ``com.amazonaws.iam#DeletePolicy``."""

from __future__ import annotations
from typing import TYPE_CHECKING
import zapros
import aws_sdk_iam._auth._signers
from aws_sdk_iam._services._pipeline import AsyncOperationOptions, OperationOptions

if TYPE_CHECKING:
    import aws_sdk_iam.types.delete_policy_request


def delete_policy(
    options: OperationOptions,
    input: aws_sdk_iam.types.delete_policy_request.DeletePolicyRequest,
) -> tuple[None, zapros.Response]:
    raise NotImplementedError("operation dispatch not yet generated")


async def async_delete_policy(
    options: AsyncOperationOptions,
    input: aws_sdk_iam.types.delete_policy_request.DeletePolicyRequest,
) -> tuple[None, zapros.Response]:
    raise NotImplementedError("operation dispatch not yet generated")
