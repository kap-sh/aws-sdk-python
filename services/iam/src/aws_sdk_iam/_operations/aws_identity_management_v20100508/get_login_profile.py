"""Generated from Smithy shape ``com.amazonaws.iam#GetLoginProfile``."""

from __future__ import annotations
from typing import TYPE_CHECKING
import zapros
import aws_sdk_iam._auth._signers
from aws_sdk_iam._services._pipeline import AsyncOperationOptions, OperationOptions

if TYPE_CHECKING:
    import aws_sdk_iam.types.get_login_profile_request
    import aws_sdk_iam.types.get_login_profile_response


def get_login_profile(
    options: OperationOptions,
    input: aws_sdk_iam.types.get_login_profile_request.GetLoginProfileRequest,
) -> tuple[
    aws_sdk_iam.types.get_login_profile_response.GetLoginProfileResponse,
    zapros.Response,
]:
    raise NotImplementedError("operation dispatch not yet generated")


async def async_get_login_profile(
    options: AsyncOperationOptions,
    input: aws_sdk_iam.types.get_login_profile_request.GetLoginProfileRequest,
) -> tuple[
    aws_sdk_iam.types.get_login_profile_response.GetLoginProfileResponse,
    zapros.Response,
]:
    raise NotImplementedError("operation dispatch not yet generated")
