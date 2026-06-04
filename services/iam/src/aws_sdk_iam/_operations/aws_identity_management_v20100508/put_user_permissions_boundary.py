"""Generated from Smithy shape ``com.amazonaws.iam#PutUserPermissionsBoundary``."""

from __future__ import annotations
from typing import TYPE_CHECKING
import zapros
import aws_sdk_iam._auth._signers
from aws_sdk_iam._services._pipeline import AsyncOperationOptions, OperationOptions

if TYPE_CHECKING:
    import aws_sdk_iam.types.put_user_permissions_boundary_request


def put_user_permissions_boundary(
    options: OperationOptions,
    input: aws_sdk_iam.types.put_user_permissions_boundary_request.PutUserPermissionsBoundaryRequest,
) -> tuple[None, zapros.Response]:
    raise NotImplementedError("operation dispatch not yet generated")


async def async_put_user_permissions_boundary(
    options: AsyncOperationOptions,
    input: aws_sdk_iam.types.put_user_permissions_boundary_request.PutUserPermissionsBoundaryRequest,
) -> tuple[None, zapros.Response]:
    raise NotImplementedError("operation dispatch not yet generated")
