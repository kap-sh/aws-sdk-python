"""Generated from Smithy shape ``com.amazonaws.kms#GenerateMac``."""

from __future__ import annotations
from typing import TYPE_CHECKING
import zapros
import awd_sdk_kms._auth._signers
from awd_sdk_kms._services._pipeline import AsyncOperationOptions, OperationOptions

if TYPE_CHECKING:
    import awd_sdk_kms.types.generate_mac_request
    import awd_sdk_kms.types.generate_mac_response


def generate_mac(
    options: OperationOptions,
    input: awd_sdk_kms.types.generate_mac_request.GenerateMacRequest,
) -> tuple[
    awd_sdk_kms.types.generate_mac_response.GenerateMacResponse, zapros.Response
]:
    raise NotImplementedError("operation dispatch not yet generated")


async def async_generate_mac(
    options: AsyncOperationOptions,
    input: awd_sdk_kms.types.generate_mac_request.GenerateMacRequest,
) -> tuple[
    awd_sdk_kms.types.generate_mac_response.GenerateMacResponse, zapros.Response
]:
    raise NotImplementedError("operation dispatch not yet generated")
