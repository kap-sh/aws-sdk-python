"""Generated from Smithy shape ``com.amazonaws.iam#DeleteLoginProfile``."""

from __future__ import annotations
from typing import TYPE_CHECKING
import zapros
import aws_sdk_iam._auth._signers
from aws_sdk_iam._services._pipeline import AsyncOperationOptions, OperationOptions

if TYPE_CHECKING:
    import aws_sdk_iam.types.delete_login_profile_request


def delete_login_profile(
    options: OperationOptions,
    input: aws_sdk_iam.types.delete_login_profile_request.DeleteLoginProfileRequest,
) -> tuple[None, zapros.Response]:
    raise NotImplementedError("operation dispatch not yet generated")


async def async_delete_login_profile(
    options: AsyncOperationOptions,
    input: aws_sdk_iam.types.delete_login_profile_request.DeleteLoginProfileRequest,
) -> tuple[None, zapros.Response]:
    raise NotImplementedError("operation dispatch not yet generated")
