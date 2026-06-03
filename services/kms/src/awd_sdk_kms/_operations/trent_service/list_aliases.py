"""Generated from Smithy shape ``com.amazonaws.kms#ListAliases``."""

from __future__ import annotations
from typing import TYPE_CHECKING
import zapros
import awd_sdk_kms._auth._signers
from awd_sdk_kms._services._pipeline import AsyncOperationOptions, OperationOptions

if TYPE_CHECKING:
    import awd_sdk_kms.types.list_aliases_request
    import awd_sdk_kms.types.list_aliases_response


def list_aliases(
    options: OperationOptions,
    input: awd_sdk_kms.types.list_aliases_request.ListAliasesRequest,
) -> tuple[
    awd_sdk_kms.types.list_aliases_response.ListAliasesResponse, zapros.Response
]:
    raise NotImplementedError("operation dispatch not yet generated")


async def async_list_aliases(
    options: AsyncOperationOptions,
    input: awd_sdk_kms.types.list_aliases_request.ListAliasesRequest,
) -> tuple[
    awd_sdk_kms.types.list_aliases_response.ListAliasesResponse, zapros.Response
]:
    raise NotImplementedError("operation dispatch not yet generated")
