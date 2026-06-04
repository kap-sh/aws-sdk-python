"""Generated from Smithy shape ``com.amazonaws.iam#DeleteGroup``."""

from __future__ import annotations
from typing import TYPE_CHECKING
import zapros
import aws_sdk_iam._auth._signers
from aws_sdk_iam._services._pipeline import AsyncOperationOptions, OperationOptions

if TYPE_CHECKING:
    import aws_sdk_iam.types.delete_group_request


def delete_group(
    options: OperationOptions,
    input: aws_sdk_iam.types.delete_group_request.DeleteGroupRequest,
) -> tuple[None, zapros.Response]:
    raise NotImplementedError("operation dispatch not yet generated")


async def async_delete_group(
    options: AsyncOperationOptions,
    input: aws_sdk_iam.types.delete_group_request.DeleteGroupRequest,
) -> tuple[None, zapros.Response]:
    raise NotImplementedError("operation dispatch not yet generated")
