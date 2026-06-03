"""Generated from Smithy shape ``com.amazonaws.kms#PutKeyPolicy``."""

from __future__ import annotations
from typing import TYPE_CHECKING
import zapros
import aws_sdk_kms._auth._signers
from aws_sdk_kms._services._pipeline import AsyncOperationOptions, OperationOptions

if TYPE_CHECKING:
    import aws_sdk_kms.types.put_key_policy_request


def put_key_policy(
    options: OperationOptions,
    input: aws_sdk_kms.types.put_key_policy_request.PutKeyPolicyRequest,
) -> tuple[None, zapros.Response]:
    raise NotImplementedError("operation dispatch not yet generated")


async def async_put_key_policy(
    options: AsyncOperationOptions,
    input: aws_sdk_kms.types.put_key_policy_request.PutKeyPolicyRequest,
) -> tuple[None, zapros.Response]:
    raise NotImplementedError("operation dispatch not yet generated")
