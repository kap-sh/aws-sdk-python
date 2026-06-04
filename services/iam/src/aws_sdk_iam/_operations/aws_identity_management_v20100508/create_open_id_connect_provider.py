"""Generated from Smithy shape ``com.amazonaws.iam#CreateOpenIDConnectProvider``."""

from __future__ import annotations
from typing import TYPE_CHECKING
import zapros
import aws_sdk_iam._auth._signers
from aws_sdk_iam._services._pipeline import AsyncOperationOptions, OperationOptions

if TYPE_CHECKING:
    import aws_sdk_iam.types.create_open_id_connect_provider_request
    import aws_sdk_iam.types.create_open_id_connect_provider_response


def create_open_id_connect_provider(
    options: OperationOptions,
    input: aws_sdk_iam.types.create_open_id_connect_provider_request.CreateOpenIDConnectProviderRequest,
) -> tuple[
    aws_sdk_iam.types.create_open_id_connect_provider_response.CreateOpenIDConnectProviderResponse,
    zapros.Response,
]:
    raise NotImplementedError("operation dispatch not yet generated")


async def async_create_open_id_connect_provider(
    options: AsyncOperationOptions,
    input: aws_sdk_iam.types.create_open_id_connect_provider_request.CreateOpenIDConnectProviderRequest,
) -> tuple[
    aws_sdk_iam.types.create_open_id_connect_provider_response.CreateOpenIDConnectProviderResponse,
    zapros.Response,
]:
    raise NotImplementedError("operation dispatch not yet generated")
