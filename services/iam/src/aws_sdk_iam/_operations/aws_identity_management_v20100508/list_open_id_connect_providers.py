"""Generated from Smithy shape ``com.amazonaws.iam#ListOpenIDConnectProviders``."""

from __future__ import annotations
from typing import TYPE_CHECKING
import zapros
import aws_sdk_iam._auth._signers
from aws_sdk_iam._services._pipeline import AsyncOperationOptions, OperationOptions

if TYPE_CHECKING:
    import aws_sdk_iam.types.list_open_id_connect_providers_request
    import aws_sdk_iam.types.list_open_id_connect_providers_response


def list_open_id_connect_providers(
    options: OperationOptions,
    input: aws_sdk_iam.types.list_open_id_connect_providers_request.ListOpenIDConnectProvidersRequest,
) -> tuple[
    aws_sdk_iam.types.list_open_id_connect_providers_response.ListOpenIDConnectProvidersResponse,
    zapros.Response,
]:
    raise NotImplementedError("operation dispatch not yet generated")


async def async_list_open_id_connect_providers(
    options: AsyncOperationOptions,
    input: aws_sdk_iam.types.list_open_id_connect_providers_request.ListOpenIDConnectProvidersRequest,
) -> tuple[
    aws_sdk_iam.types.list_open_id_connect_providers_response.ListOpenIDConnectProvidersResponse,
    zapros.Response,
]:
    raise NotImplementedError("operation dispatch not yet generated")
