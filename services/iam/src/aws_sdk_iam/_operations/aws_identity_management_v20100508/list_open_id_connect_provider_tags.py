"""Generated from Smithy shape ``com.amazonaws.iam#ListOpenIDConnectProviderTags``."""

from __future__ import annotations
from typing import TYPE_CHECKING
import zapros
import aws_sdk_iam._auth._signers
from aws_sdk_iam._services._pipeline import AsyncOperationOptions, OperationOptions

if TYPE_CHECKING:
    import aws_sdk_iam.types.list_open_id_connect_provider_tags_request
    import aws_sdk_iam.types.list_open_id_connect_provider_tags_response


def list_open_id_connect_provider_tags(
    options: OperationOptions,
    input: aws_sdk_iam.types.list_open_id_connect_provider_tags_request.ListOpenIDConnectProviderTagsRequest,
) -> tuple[
    aws_sdk_iam.types.list_open_id_connect_provider_tags_response.ListOpenIDConnectProviderTagsResponse,
    zapros.Response,
]:
    raise NotImplementedError("operation dispatch not yet generated")


async def async_list_open_id_connect_provider_tags(
    options: AsyncOperationOptions,
    input: aws_sdk_iam.types.list_open_id_connect_provider_tags_request.ListOpenIDConnectProviderTagsRequest,
) -> tuple[
    aws_sdk_iam.types.list_open_id_connect_provider_tags_response.ListOpenIDConnectProviderTagsResponse,
    zapros.Response,
]:
    raise NotImplementedError("operation dispatch not yet generated")
