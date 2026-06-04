"""Generated from Smithy shape ``com.amazonaws.iam#ResetServiceSpecificCredential``."""

from __future__ import annotations
from typing import TYPE_CHECKING
import zapros
import aws_sdk_iam._auth._signers
from aws_sdk_iam._services._pipeline import AsyncOperationOptions, OperationOptions

if TYPE_CHECKING:
    import aws_sdk_iam.types.reset_service_specific_credential_request
    import aws_sdk_iam.types.reset_service_specific_credential_response


def reset_service_specific_credential(
    options: OperationOptions,
    input: aws_sdk_iam.types.reset_service_specific_credential_request.ResetServiceSpecificCredentialRequest,
) -> tuple[
    aws_sdk_iam.types.reset_service_specific_credential_response.ResetServiceSpecificCredentialResponse,
    zapros.Response,
]:
    raise NotImplementedError("operation dispatch not yet generated")


async def async_reset_service_specific_credential(
    options: AsyncOperationOptions,
    input: aws_sdk_iam.types.reset_service_specific_credential_request.ResetServiceSpecificCredentialRequest,
) -> tuple[
    aws_sdk_iam.types.reset_service_specific_credential_response.ResetServiceSpecificCredentialResponse,
    zapros.Response,
]:
    raise NotImplementedError("operation dispatch not yet generated")
