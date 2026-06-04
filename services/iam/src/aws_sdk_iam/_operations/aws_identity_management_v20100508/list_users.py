"""Generated from Smithy shape ``com.amazonaws.iam#ListUsers``."""

from __future__ import annotations
from typing import TYPE_CHECKING
import zapros
import aws_sdk_iam._auth._signers
from aws_sdk_iam._services._pipeline import AsyncOperationOptions, OperationOptions

if TYPE_CHECKING:
    import aws_sdk_iam.types.list_users_request
    import aws_sdk_iam.types.list_users_response


def list_users(
    options: OperationOptions,
    input: aws_sdk_iam.types.list_users_request.ListUsersRequest,
) -> tuple[aws_sdk_iam.types.list_users_response.ListUsersResponse, zapros.Response]:
    raise NotImplementedError("operation dispatch not yet generated")


async def async_list_users(
    options: AsyncOperationOptions,
    input: aws_sdk_iam.types.list_users_request.ListUsersRequest,
) -> tuple[aws_sdk_iam.types.list_users_response.ListUsersResponse, zapros.Response]:
    raise NotImplementedError("operation dispatch not yet generated")
