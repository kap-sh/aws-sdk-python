"""Generated from Smithy shape ``com.amazonaws.iam#ListServiceSpecificCredentials``."""

from __future__ import annotations
from typing import TYPE_CHECKING
import zapros
import aws_sdk_iam._auth._signers
from aws_sdk_iam._services._pipeline import AsyncOperationOptions, OperationOptions

if TYPE_CHECKING:
    import aws_sdk_iam.types.list_service_specific_credentials_request
    import aws_sdk_iam.types.list_service_specific_credentials_response


def list_service_specific_credentials(
    options: OperationOptions,
    input: aws_sdk_iam.types.list_service_specific_credentials_request.ListServiceSpecificCredentialsRequest,
) -> tuple[
    aws_sdk_iam.types.list_service_specific_credentials_response.ListServiceSpecificCredentialsResponse,
    zapros.Response,
]:
    raise NotImplementedError("operation dispatch not yet generated")


async def async_list_service_specific_credentials(
    options: AsyncOperationOptions,
    input: aws_sdk_iam.types.list_service_specific_credentials_request.ListServiceSpecificCredentialsRequest,
) -> tuple[
    aws_sdk_iam.types.list_service_specific_credentials_response.ListServiceSpecificCredentialsResponse,
    zapros.Response,
]:
    raise NotImplementedError("operation dispatch not yet generated")
