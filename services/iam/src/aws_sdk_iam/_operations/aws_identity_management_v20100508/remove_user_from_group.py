"""Generated from Smithy shape ``com.amazonaws.iam#RemoveUserFromGroup``."""

from __future__ import annotations
from typing import TYPE_CHECKING
import zapros
import aws_sdk_iam._auth._signers
from aws_sdk_iam._services._pipeline import AsyncOperationOptions, OperationOptions

if TYPE_CHECKING:
    import aws_sdk_iam.types.remove_user_from_group_request


def remove_user_from_group(
    options: OperationOptions,
    input: aws_sdk_iam.types.remove_user_from_group_request.RemoveUserFromGroupRequest,
) -> tuple[None, zapros.Response]:
    raise NotImplementedError("operation dispatch not yet generated")


async def async_remove_user_from_group(
    options: AsyncOperationOptions,
    input: aws_sdk_iam.types.remove_user_from_group_request.RemoveUserFromGroupRequest,
) -> tuple[None, zapros.Response]:
    raise NotImplementedError("operation dispatch not yet generated")
