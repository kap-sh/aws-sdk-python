"""Generated from Smithy shape ``com.amazonaws.iam#CreateUser``."""

from __future__ import annotations
from typing import TYPE_CHECKING
import zapros
import aws_sdk_iam._auth._signers
from aws_sdk_iam._services._pipeline import AsyncOperationOptions, OperationOptions

if TYPE_CHECKING:
    import aws_sdk_iam.types.create_user_request
    import aws_sdk_iam.types.create_user_response


def create_user(
    options: OperationOptions,
    input: aws_sdk_iam.types.create_user_request.CreateUserRequest,
) -> tuple[aws_sdk_iam.types.create_user_response.CreateUserResponse, zapros.Response]:
    raise NotImplementedError("operation dispatch not yet generated")


async def async_create_user(
    options: AsyncOperationOptions,
    input: aws_sdk_iam.types.create_user_request.CreateUserRequest,
) -> tuple[aws_sdk_iam.types.create_user_response.CreateUserResponse, zapros.Response]:
    raise NotImplementedError("operation dispatch not yet generated")
