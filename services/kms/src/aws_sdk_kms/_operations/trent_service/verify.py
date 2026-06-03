"""Generated from Smithy shape ``com.amazonaws.kms#Verify``."""

from __future__ import annotations
from typing import TYPE_CHECKING
import zapros
import aws_sdk_kms._auth._signers
from aws_sdk_kms._services._pipeline import AsyncOperationOptions, OperationOptions

if TYPE_CHECKING:
    import aws_sdk_kms.types.verify_request
    import aws_sdk_kms.types.verify_response


def verify(
    options: OperationOptions, input: aws_sdk_kms.types.verify_request.VerifyRequest
) -> tuple[aws_sdk_kms.types.verify_response.VerifyResponse, zapros.Response]:
    raise NotImplementedError("operation dispatch not yet generated")


async def async_verify(
    options: AsyncOperationOptions,
    input: aws_sdk_kms.types.verify_request.VerifyRequest,
) -> tuple[aws_sdk_kms.types.verify_response.VerifyResponse, zapros.Response]:
    raise NotImplementedError("operation dispatch not yet generated")
