"""Generated from Smithy shape ``com.amazonaws.iam#GetAccountAuthorizationDetails``."""

from __future__ import annotations
from typing import TYPE_CHECKING
import zapros
import aws_sdk_iam._auth._signers
from aws_sdk_iam._services._pipeline import AsyncOperationOptions, OperationOptions

if TYPE_CHECKING:
    import aws_sdk_iam.types.get_account_authorization_details_request
    import aws_sdk_iam.types.get_account_authorization_details_response


def get_account_authorization_details(
    options: OperationOptions,
    input: aws_sdk_iam.types.get_account_authorization_details_request.GetAccountAuthorizationDetailsRequest,
) -> tuple[
    aws_sdk_iam.types.get_account_authorization_details_response.GetAccountAuthorizationDetailsResponse,
    zapros.Response,
]:
    raise NotImplementedError("operation dispatch not yet generated")


async def async_get_account_authorization_details(
    options: AsyncOperationOptions,
    input: aws_sdk_iam.types.get_account_authorization_details_request.GetAccountAuthorizationDetailsRequest,
) -> tuple[
    aws_sdk_iam.types.get_account_authorization_details_response.GetAccountAuthorizationDetailsResponse,
    zapros.Response,
]:
    raise NotImplementedError("operation dispatch not yet generated")
