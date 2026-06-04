"""Generated from Smithy shape ``com.amazonaws.iam#TagOpenIDConnectProvider``."""

from __future__ import annotations
from typing import TYPE_CHECKING
import zapros
import aws_sdk_iam._auth._signers
from aws_sdk_iam._services._pipeline import AsyncOperationOptions, OperationOptions

if TYPE_CHECKING:
    import aws_sdk_iam.types.tag_open_id_connect_provider_request


def tag_open_id_connect_provider(
    options: OperationOptions,
    input: aws_sdk_iam.types.tag_open_id_connect_provider_request.TagOpenIDConnectProviderRequest,
) -> tuple[None, zapros.Response]:
    raise NotImplementedError("operation dispatch not yet generated")


async def async_tag_open_id_connect_provider(
    options: AsyncOperationOptions,
    input: aws_sdk_iam.types.tag_open_id_connect_provider_request.TagOpenIDConnectProviderRequest,
) -> tuple[None, zapros.Response]:
    raise NotImplementedError("operation dispatch not yet generated")
