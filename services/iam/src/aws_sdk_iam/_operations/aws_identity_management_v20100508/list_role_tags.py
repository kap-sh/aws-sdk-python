"""Generated from Smithy shape ``com.amazonaws.iam#ListRoleTags``."""

from __future__ import annotations
from typing import TYPE_CHECKING
import zapros
import aws_sdk_iam._auth._signers
from aws_sdk_iam._services._pipeline import AsyncOperationOptions, OperationOptions

if TYPE_CHECKING:
    import aws_sdk_iam.types.list_role_tags_request
    import aws_sdk_iam.types.list_role_tags_response


def list_role_tags(
    options: OperationOptions,
    input: aws_sdk_iam.types.list_role_tags_request.ListRoleTagsRequest,
) -> tuple[
    aws_sdk_iam.types.list_role_tags_response.ListRoleTagsResponse, zapros.Response
]:
    raise NotImplementedError("operation dispatch not yet generated")


async def async_list_role_tags(
    options: AsyncOperationOptions,
    input: aws_sdk_iam.types.list_role_tags_request.ListRoleTagsRequest,
) -> tuple[
    aws_sdk_iam.types.list_role_tags_response.ListRoleTagsResponse, zapros.Response
]:
    raise NotImplementedError("operation dispatch not yet generated")
