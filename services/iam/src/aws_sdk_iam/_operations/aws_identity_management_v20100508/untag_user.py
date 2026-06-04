"""Generated from Smithy shape ``com.amazonaws.iam#UntagUser``."""

from __future__ import annotations
from typing import TYPE_CHECKING
import zapros
import aws_sdk_iam._auth._signers
from aws_sdk_iam._services._pipeline import AsyncOperationOptions, OperationOptions

if TYPE_CHECKING:
    import aws_sdk_iam.types.untag_user_request


def untag_user(
    options: OperationOptions,
    input: aws_sdk_iam.types.untag_user_request.UntagUserRequest,
) -> tuple[None, zapros.Response]:
    raise NotImplementedError("operation dispatch not yet generated")


async def async_untag_user(
    options: AsyncOperationOptions,
    input: aws_sdk_iam.types.untag_user_request.UntagUserRequest,
) -> tuple[None, zapros.Response]:
    raise NotImplementedError("operation dispatch not yet generated")
