"""Generated from Smithy shape ``com.amazonaws.kms#ListKeyRotations``."""

from __future__ import annotations
from typing import TYPE_CHECKING
import zapros
import awd_sdk_kms._auth._signers
from awd_sdk_kms._services._pipeline import AsyncOperationOptions, OperationOptions

if TYPE_CHECKING:
    import awd_sdk_kms.types.list_key_rotations_request
    import awd_sdk_kms.types.list_key_rotations_response


def list_key_rotations(
    options: OperationOptions,
    input: awd_sdk_kms.types.list_key_rotations_request.ListKeyRotationsRequest,
) -> tuple[
    awd_sdk_kms.types.list_key_rotations_response.ListKeyRotationsResponse,
    zapros.Response,
]:
    raise NotImplementedError("operation dispatch not yet generated")


async def async_list_key_rotations(
    options: AsyncOperationOptions,
    input: awd_sdk_kms.types.list_key_rotations_request.ListKeyRotationsRequest,
) -> tuple[
    awd_sdk_kms.types.list_key_rotations_response.ListKeyRotationsResponse,
    zapros.Response,
]:
    raise NotImplementedError("operation dispatch not yet generated")
