"""Generated from Smithy shape ``com.amazonaws.iam#ListGroupsForUser``."""

from __future__ import annotations
from typing import TYPE_CHECKING
import zapros
import aws_sdk_iam._auth._signers
from aws_sdk_iam._services._pipeline import AsyncOperationOptions, OperationOptions

if TYPE_CHECKING:
    import aws_sdk_iam.types.list_groups_for_user_request
    import aws_sdk_iam.types.list_groups_for_user_response


def list_groups_for_user(
    options: OperationOptions,
    input: aws_sdk_iam.types.list_groups_for_user_request.ListGroupsForUserRequest,
) -> tuple[
    aws_sdk_iam.types.list_groups_for_user_response.ListGroupsForUserResponse,
    zapros.Response,
]:
    raise NotImplementedError("operation dispatch not yet generated")


async def async_list_groups_for_user(
    options: AsyncOperationOptions,
    input: aws_sdk_iam.types.list_groups_for_user_request.ListGroupsForUserRequest,
) -> tuple[
    aws_sdk_iam.types.list_groups_for_user_response.ListGroupsForUserResponse,
    zapros.Response,
]:
    raise NotImplementedError("operation dispatch not yet generated")
