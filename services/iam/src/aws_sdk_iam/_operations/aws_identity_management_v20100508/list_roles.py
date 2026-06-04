"""Generated from Smithy shape ``com.amazonaws.iam#ListRoles``."""

from __future__ import annotations
from typing import TYPE_CHECKING
import zapros
import aws_sdk_iam._auth._signers
from aws_sdk_iam._services._pipeline import AsyncOperationOptions, OperationOptions

if TYPE_CHECKING:
    import aws_sdk_iam.types.list_roles_request
    import aws_sdk_iam.types.list_roles_response


def list_roles(
    options: OperationOptions,
    input: aws_sdk_iam.types.list_roles_request.ListRolesRequest,
) -> tuple[aws_sdk_iam.types.list_roles_response.ListRolesResponse, zapros.Response]:
    raise NotImplementedError("operation dispatch not yet generated")


async def async_list_roles(
    options: AsyncOperationOptions,
    input: aws_sdk_iam.types.list_roles_request.ListRolesRequest,
) -> tuple[aws_sdk_iam.types.list_roles_response.ListRolesResponse, zapros.Response]:
    raise NotImplementedError("operation dispatch not yet generated")
