"""Generated from Smithy shape ``com.amazonaws.kms#ListRetirableGrants``."""

from __future__ import annotations
from typing import TYPE_CHECKING
import zapros
import awd_sdk_kms._auth._signers
from awd_sdk_kms._services._pipeline import AsyncOperationOptions, OperationOptions

if TYPE_CHECKING:
    import awd_sdk_kms.types.list_retirable_grants_request
    import awd_sdk_kms.types.list_grants_response


def list_retirable_grants(
    options: OperationOptions,
    input: awd_sdk_kms.types.list_retirable_grants_request.ListRetirableGrantsRequest,
) -> tuple[awd_sdk_kms.types.list_grants_response.ListGrantsResponse, zapros.Response]:
    raise NotImplementedError("operation dispatch not yet generated")


async def async_list_retirable_grants(
    options: AsyncOperationOptions,
    input: awd_sdk_kms.types.list_retirable_grants_request.ListRetirableGrantsRequest,
) -> tuple[awd_sdk_kms.types.list_grants_response.ListGrantsResponse, zapros.Response]:
    raise NotImplementedError("operation dispatch not yet generated")
