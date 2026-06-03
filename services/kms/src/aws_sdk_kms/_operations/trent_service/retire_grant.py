"""Generated from Smithy shape ``com.amazonaws.kms#RetireGrant``."""

from __future__ import annotations
from typing import TYPE_CHECKING
import zapros
import aws_sdk_kms._auth._signers
from aws_sdk_kms._services._pipeline import AsyncOperationOptions, OperationOptions

if TYPE_CHECKING:
    import aws_sdk_kms.types.retire_grant_request


def retire_grant(
    options: OperationOptions,
    input: aws_sdk_kms.types.retire_grant_request.RetireGrantRequest,
) -> tuple[None, zapros.Response]:
    raise NotImplementedError("operation dispatch not yet generated")


async def async_retire_grant(
    options: AsyncOperationOptions,
    input: aws_sdk_kms.types.retire_grant_request.RetireGrantRequest,
) -> tuple[None, zapros.Response]:
    raise NotImplementedError("operation dispatch not yet generated")
