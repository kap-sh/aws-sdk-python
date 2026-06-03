"""Generated from Smithy shape ``com.amazonaws.kms#UpdatePrimaryRegion``."""

from __future__ import annotations
from typing import TYPE_CHECKING
import zapros
import awd_sdk_kms._auth._signers
from awd_sdk_kms._services._pipeline import AsyncOperationOptions, OperationOptions

if TYPE_CHECKING:
    import awd_sdk_kms.types.update_primary_region_request


def update_primary_region(
    options: OperationOptions,
    input: awd_sdk_kms.types.update_primary_region_request.UpdatePrimaryRegionRequest,
) -> tuple[None, zapros.Response]:
    raise NotImplementedError("operation dispatch not yet generated")


async def async_update_primary_region(
    options: AsyncOperationOptions,
    input: awd_sdk_kms.types.update_primary_region_request.UpdatePrimaryRegionRequest,
) -> tuple[None, zapros.Response]:
    raise NotImplementedError("operation dispatch not yet generated")
