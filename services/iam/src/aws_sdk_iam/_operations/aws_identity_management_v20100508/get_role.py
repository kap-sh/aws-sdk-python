"""Generated from Smithy shape ``com.amazonaws.iam#GetRole``."""

from __future__ import annotations
from typing import TYPE_CHECKING
import zapros
import aws_sdk_iam._auth._signers
from aws_sdk_iam._services._pipeline import AsyncOperationOptions, OperationOptions

if TYPE_CHECKING:
    import aws_sdk_iam.types.get_role_request
    import aws_sdk_iam.types.get_role_response


def get_role(
    options: OperationOptions, input: aws_sdk_iam.types.get_role_request.GetRoleRequest
) -> tuple[aws_sdk_iam.types.get_role_response.GetRoleResponse, zapros.Response]:
    raise NotImplementedError("operation dispatch not yet generated")


async def async_get_role(
    options: AsyncOperationOptions,
    input: aws_sdk_iam.types.get_role_request.GetRoleRequest,
) -> tuple[aws_sdk_iam.types.get_role_response.GetRoleResponse, zapros.Response]:
    raise NotImplementedError("operation dispatch not yet generated")
