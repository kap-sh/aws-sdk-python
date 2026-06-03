"""Generated from Smithy shape ``com.amazonaws.kms#GenerateRandom``."""

from __future__ import annotations
from typing import TYPE_CHECKING
import zapros
import awd_sdk_kms._auth._signers
from awd_sdk_kms._services._pipeline import AsyncOperationOptions, OperationOptions

if TYPE_CHECKING:
    import awd_sdk_kms.types.generate_random_request
    import awd_sdk_kms.types.generate_random_response


def generate_random(
    options: OperationOptions,
    input: awd_sdk_kms.types.generate_random_request.GenerateRandomRequest,
) -> tuple[
    awd_sdk_kms.types.generate_random_response.GenerateRandomResponse, zapros.Response
]:
    raise NotImplementedError("operation dispatch not yet generated")


async def async_generate_random(
    options: AsyncOperationOptions,
    input: awd_sdk_kms.types.generate_random_request.GenerateRandomRequest,
) -> tuple[
    awd_sdk_kms.types.generate_random_response.GenerateRandomResponse, zapros.Response
]:
    raise NotImplementedError("operation dispatch not yet generated")
