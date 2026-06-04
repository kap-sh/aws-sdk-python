"""Generated from Smithy shape ``com.amazonaws.iam#CreateServiceSpecificCredential``."""

from __future__ import annotations
from typing import TYPE_CHECKING
import zapros
import aws_sdk_iam._auth._signers
from aws_sdk_iam._services._pipeline import AsyncOperationOptions, OperationOptions

if TYPE_CHECKING:
    import aws_sdk_iam.types.create_service_specific_credential_request
    import aws_sdk_iam.types.create_service_specific_credential_response


def create_service_specific_credential(
    options: OperationOptions,
    input: aws_sdk_iam.types.create_service_specific_credential_request.CreateServiceSpecificCredentialRequest,
) -> tuple[
    aws_sdk_iam.types.create_service_specific_credential_response.CreateServiceSpecificCredentialResponse,
    zapros.Response,
]:
    raise NotImplementedError("operation dispatch not yet generated")


async def async_create_service_specific_credential(
    options: AsyncOperationOptions,
    input: aws_sdk_iam.types.create_service_specific_credential_request.CreateServiceSpecificCredentialRequest,
) -> tuple[
    aws_sdk_iam.types.create_service_specific_credential_response.CreateServiceSpecificCredentialResponse,
    zapros.Response,
]:
    raise NotImplementedError("operation dispatch not yet generated")
