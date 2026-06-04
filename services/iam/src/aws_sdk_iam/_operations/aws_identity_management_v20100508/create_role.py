"""Generated from Smithy shape ``com.amazonaws.iam#CreateRole``."""

from __future__ import annotations
from typing import TYPE_CHECKING
import zapros
import aws_sdk_iam._auth._signers
from aws_sdk_iam._services._pipeline import AsyncOperationOptions, OperationOptions

if TYPE_CHECKING:
    import aws_sdk_iam.types.create_role_request
    import aws_sdk_iam.types.create_role_response


def create_role(
    options: OperationOptions,
    input: aws_sdk_iam.types.create_role_request.CreateRoleRequest,
) -> tuple[aws_sdk_iam.types.create_role_response.CreateRoleResponse, zapros.Response]:
    raise NotImplementedError("operation dispatch not yet generated")


async def async_create_role(
    options: AsyncOperationOptions,
    input: aws_sdk_iam.types.create_role_request.CreateRoleRequest,
) -> tuple[aws_sdk_iam.types.create_role_response.CreateRoleResponse, zapros.Response]:
    raise NotImplementedError("operation dispatch not yet generated")
