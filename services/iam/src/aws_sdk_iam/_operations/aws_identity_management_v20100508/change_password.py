"""Generated from Smithy shape ``com.amazonaws.iam#ChangePassword``."""

from __future__ import annotations
from typing import TYPE_CHECKING
import zapros
import aws_sdk_iam._auth._signers
from aws_sdk_iam._services._pipeline import AsyncOperationOptions, OperationOptions

if TYPE_CHECKING:
    import aws_sdk_iam.types.change_password_request


def change_password(
    options: OperationOptions,
    input: aws_sdk_iam.types.change_password_request.ChangePasswordRequest,
) -> tuple[None, zapros.Response]:
    raise NotImplementedError("operation dispatch not yet generated")


async def async_change_password(
    options: AsyncOperationOptions,
    input: aws_sdk_iam.types.change_password_request.ChangePasswordRequest,
) -> tuple[None, zapros.Response]:
    raise NotImplementedError("operation dispatch not yet generated")
