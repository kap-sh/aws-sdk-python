"""Generated from Smithy shape ``com.amazonaws.iam#DeleteUserPermissionsBoundary``."""

from __future__ import annotations
from typing import TYPE_CHECKING
import zapros
import aws_sdk_iam._auth._signers
from aws_sdk_iam._services._pipeline import AsyncOperationOptions, OperationOptions

if TYPE_CHECKING:
    import aws_sdk_iam.types.delete_user_permissions_boundary_request


def delete_user_permissions_boundary(
    options: OperationOptions,
    input: aws_sdk_iam.types.delete_user_permissions_boundary_request.DeleteUserPermissionsBoundaryRequest,
) -> tuple[None, zapros.Response]:
    raise NotImplementedError("operation dispatch not yet generated")


async def async_delete_user_permissions_boundary(
    options: AsyncOperationOptions,
    input: aws_sdk_iam.types.delete_user_permissions_boundary_request.DeleteUserPermissionsBoundaryRequest,
) -> tuple[None, zapros.Response]:
    raise NotImplementedError("operation dispatch not yet generated")
