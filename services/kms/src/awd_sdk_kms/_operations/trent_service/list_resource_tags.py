"""Generated from Smithy shape ``com.amazonaws.kms#ListResourceTags``."""

from __future__ import annotations
from typing import TYPE_CHECKING
import zapros
import awd_sdk_kms._auth._signers
from awd_sdk_kms._services._pipeline import AsyncOperationOptions, OperationOptions

if TYPE_CHECKING:
    import awd_sdk_kms.types.list_resource_tags_request
    import awd_sdk_kms.types.list_resource_tags_response


def list_resource_tags(
    options: OperationOptions,
    input: awd_sdk_kms.types.list_resource_tags_request.ListResourceTagsRequest,
) -> tuple[
    awd_sdk_kms.types.list_resource_tags_response.ListResourceTagsResponse,
    zapros.Response,
]:
    raise NotImplementedError("operation dispatch not yet generated")


async def async_list_resource_tags(
    options: AsyncOperationOptions,
    input: awd_sdk_kms.types.list_resource_tags_request.ListResourceTagsRequest,
) -> tuple[
    awd_sdk_kms.types.list_resource_tags_response.ListResourceTagsResponse,
    zapros.Response,
]:
    raise NotImplementedError("operation dispatch not yet generated")
