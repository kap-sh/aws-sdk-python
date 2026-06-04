"""Generated from Smithy shape ``com.amazonaws.iam#AddUserToGroup``."""

from __future__ import annotations
from typing import TYPE_CHECKING
import zapros
import aws_sdk_iam._auth._signers
from aws_sdk_iam._services._pipeline import AsyncOperationOptions, OperationOptions

if TYPE_CHECKING:
    import aws_sdk_iam.types.add_user_to_group_request


def add_user_to_group(
    options: OperationOptions,
    input: aws_sdk_iam.types.add_user_to_group_request.AddUserToGroupRequest,
) -> tuple[None, zapros.Response]:
    raise NotImplementedError("operation dispatch not yet generated")


async def async_add_user_to_group(
    options: AsyncOperationOptions,
    input: aws_sdk_iam.types.add_user_to_group_request.AddUserToGroupRequest,
) -> tuple[None, zapros.Response]:
    raise NotImplementedError("operation dispatch not yet generated")
