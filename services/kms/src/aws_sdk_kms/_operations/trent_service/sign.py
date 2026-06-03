"""Generated from Smithy shape ``com.amazonaws.kms#Sign``."""

from __future__ import annotations
from typing import TYPE_CHECKING
import zapros
import aws_sdk_kms._auth._signers
from aws_sdk_kms._services._pipeline import AsyncOperationOptions, OperationOptions

if TYPE_CHECKING:
    import aws_sdk_kms.types.sign_request
    import aws_sdk_kms.types.sign_response


def sign(
    options: OperationOptions, input: aws_sdk_kms.types.sign_request.SignRequest
) -> tuple[aws_sdk_kms.types.sign_response.SignResponse, zapros.Response]:
    raise NotImplementedError("operation dispatch not yet generated")


async def async_sign(
    options: AsyncOperationOptions, input: aws_sdk_kms.types.sign_request.SignRequest
) -> tuple[aws_sdk_kms.types.sign_response.SignResponse, zapros.Response]:
    raise NotImplementedError("operation dispatch not yet generated")
