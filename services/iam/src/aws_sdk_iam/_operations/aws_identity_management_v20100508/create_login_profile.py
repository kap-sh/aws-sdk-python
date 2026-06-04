"""Generated from Smithy shape ``com.amazonaws.iam#CreateLoginProfile``."""

from __future__ import annotations
from typing import TYPE_CHECKING
import zapros
import aws_sdk_iam._auth._signers
from aws_sdk_iam._services._pipeline import AsyncOperationOptions, OperationOptions

if TYPE_CHECKING:
    import aws_sdk_iam.types.create_login_profile_request
    import aws_sdk_iam.types.create_login_profile_response


def create_login_profile(
    options: OperationOptions,
    input: aws_sdk_iam.types.create_login_profile_request.CreateLoginProfileRequest,
) -> tuple[
    aws_sdk_iam.types.create_login_profile_response.CreateLoginProfileResponse,
    zapros.Response,
]:
    raise NotImplementedError("operation dispatch not yet generated")


async def async_create_login_profile(
    options: AsyncOperationOptions,
    input: aws_sdk_iam.types.create_login_profile_request.CreateLoginProfileRequest,
) -> tuple[
    aws_sdk_iam.types.create_login_profile_response.CreateLoginProfileResponse,
    zapros.Response,
]:
    raise NotImplementedError("operation dispatch not yet generated")
