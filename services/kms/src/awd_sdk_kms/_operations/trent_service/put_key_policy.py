"""Generated from Smithy shape ``com.amazonaws.kms#PutKeyPolicy``."""

from __future__ import annotations
from typing import TYPE_CHECKING
import zapros
import awd_sdk_kms._auth._signers
from awd_sdk_kms._services._pipeline import AsyncOperationOptions, OperationOptions

if TYPE_CHECKING:
    import awd_sdk_kms.types.put_key_policy_request


def put_key_policy(
    options: OperationOptions,
    input: awd_sdk_kms.types.put_key_policy_request.PutKeyPolicyRequest,
) -> tuple[None, zapros.Response]:
    raise NotImplementedError("operation dispatch not yet generated")


async def async_put_key_policy(
    options: AsyncOperationOptions,
    input: awd_sdk_kms.types.put_key_policy_request.PutKeyPolicyRequest,
) -> tuple[None, zapros.Response]:
    raise NotImplementedError("operation dispatch not yet generated")
