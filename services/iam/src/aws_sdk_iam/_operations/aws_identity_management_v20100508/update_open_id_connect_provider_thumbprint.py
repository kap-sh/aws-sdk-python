"""Generated from Smithy shape ``com.amazonaws.iam#UpdateOpenIDConnectProviderThumbprint``."""

from __future__ import annotations
from typing import TYPE_CHECKING
import zapros
import aws_sdk_iam._auth._signers
from aws_sdk_iam._services._pipeline import AsyncOperationOptions, OperationOptions

if TYPE_CHECKING:
    import aws_sdk_iam.types.update_open_id_connect_provider_thumbprint_request


def update_open_id_connect_provider_thumbprint(
    options: OperationOptions,
    input: aws_sdk_iam.types.update_open_id_connect_provider_thumbprint_request.UpdateOpenIDConnectProviderThumbprintRequest,
) -> tuple[None, zapros.Response]:
    raise NotImplementedError("operation dispatch not yet generated")


async def async_update_open_id_connect_provider_thumbprint(
    options: AsyncOperationOptions,
    input: aws_sdk_iam.types.update_open_id_connect_provider_thumbprint_request.UpdateOpenIDConnectProviderThumbprintRequest,
) -> tuple[None, zapros.Response]:
    raise NotImplementedError("operation dispatch not yet generated")
