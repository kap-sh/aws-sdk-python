"""Generated from Smithy shape ``com.amazonaws.iam#UpdateRole``."""

from __future__ import annotations
from typing import TYPE_CHECKING
import zapros
import aws_sdk_iam._auth._signers
from aws_sdk_iam._services._pipeline import AsyncOperationOptions, OperationOptions

if TYPE_CHECKING:
    import aws_sdk_iam.types.update_role_request
    import aws_sdk_iam.types.update_role_response


def update_role(
    options: OperationOptions,
    input: aws_sdk_iam.types.update_role_request.UpdateRoleRequest,
) -> tuple[aws_sdk_iam.types.update_role_response.UpdateRoleResponse, zapros.Response]:
    raise NotImplementedError("operation dispatch not yet generated")


async def async_update_role(
    options: AsyncOperationOptions,
    input: aws_sdk_iam.types.update_role_request.UpdateRoleRequest,
) -> tuple[aws_sdk_iam.types.update_role_response.UpdateRoleResponse, zapros.Response]:
    raise NotImplementedError("operation dispatch not yet generated")
