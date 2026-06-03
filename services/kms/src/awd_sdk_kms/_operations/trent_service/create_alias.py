"""Generated from Smithy shape ``com.amazonaws.kms#CreateAlias``."""

from __future__ import annotations
from typing import TYPE_CHECKING
import zapros
import awd_sdk_kms._auth._signers
from awd_sdk_kms._services._pipeline import AsyncOperationOptions, OperationOptions

if TYPE_CHECKING:
    import awd_sdk_kms.types.create_alias_request


def create_alias(
    options: OperationOptions,
    input: awd_sdk_kms.types.create_alias_request.CreateAliasRequest,
) -> tuple[None, zapros.Response]:
    raise NotImplementedError("operation dispatch not yet generated")


async def async_create_alias(
    options: AsyncOperationOptions,
    input: awd_sdk_kms.types.create_alias_request.CreateAliasRequest,
) -> tuple[None, zapros.Response]:
    raise NotImplementedError("operation dispatch not yet generated")
