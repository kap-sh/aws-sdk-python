"""Generated from Smithy shape ``com.amazonaws.kms#VerifyMac``."""

from __future__ import annotations
from typing import TYPE_CHECKING
import zapros
import awd_sdk_kms._auth._signers
from awd_sdk_kms._services._pipeline import AsyncOperationOptions, OperationOptions

if TYPE_CHECKING:
    import awd_sdk_kms.types.verify_mac_request
    import awd_sdk_kms.types.verify_mac_response


def verify_mac(
    options: OperationOptions,
    input: awd_sdk_kms.types.verify_mac_request.VerifyMacRequest,
) -> tuple[awd_sdk_kms.types.verify_mac_response.VerifyMacResponse, zapros.Response]:
    raise NotImplementedError("operation dispatch not yet generated")


async def async_verify_mac(
    options: AsyncOperationOptions,
    input: awd_sdk_kms.types.verify_mac_request.VerifyMacRequest,
) -> tuple[awd_sdk_kms.types.verify_mac_response.VerifyMacResponse, zapros.Response]:
    raise NotImplementedError("operation dispatch not yet generated")
