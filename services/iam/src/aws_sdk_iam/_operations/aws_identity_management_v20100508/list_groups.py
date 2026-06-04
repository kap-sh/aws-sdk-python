"""Generated from Smithy shape ``com.amazonaws.iam#ListGroups``."""

from __future__ import annotations
from typing import TYPE_CHECKING
import zapros
import aws_sdk_iam._auth._signers
from aws_sdk_iam._services._pipeline import AsyncOperationOptions, OperationOptions

if TYPE_CHECKING:
    import aws_sdk_iam.types.list_groups_request
    import aws_sdk_iam.types.list_groups_response


def list_groups(
    options: OperationOptions,
    input: aws_sdk_iam.types.list_groups_request.ListGroupsRequest,
) -> tuple[aws_sdk_iam.types.list_groups_response.ListGroupsResponse, zapros.Response]:
    raise NotImplementedError("operation dispatch not yet generated")


async def async_list_groups(
    options: AsyncOperationOptions,
    input: aws_sdk_iam.types.list_groups_request.ListGroupsRequest,
) -> tuple[aws_sdk_iam.types.list_groups_response.ListGroupsResponse, zapros.Response]:
    raise NotImplementedError("operation dispatch not yet generated")
