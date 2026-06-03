"""Generated from Smithy shape ``com.amazonaws.kms#Sign``."""

from __future__ import annotations
from typing import TYPE_CHECKING
import zapros
import awd_sdk_kms._auth._signers
from awd_sdk_kms._services._pipeline import AsyncOperationOptions, OperationOptions

if TYPE_CHECKING:
    import awd_sdk_kms.types.sign_request
    import awd_sdk_kms.types.sign_response


def sign(
    options: OperationOptions, input: awd_sdk_kms.types.sign_request.SignRequest
) -> tuple[awd_sdk_kms.types.sign_response.SignResponse, zapros.Response]:
    raise NotImplementedError("operation dispatch not yet generated")


async def async_sign(
    options: AsyncOperationOptions, input: awd_sdk_kms.types.sign_request.SignRequest
) -> tuple[awd_sdk_kms.types.sign_response.SignResponse, zapros.Response]:
    raise NotImplementedError("operation dispatch not yet generated")
