"""Generated from Smithy shape ``com.amazonaws.iam#DeleteServiceSpecificCredential``."""

from __future__ import annotations
from typing import TYPE_CHECKING
import zapros
import aws_sdk_iam._auth._signers
from aws_sdk_iam._services._pipeline import AsyncOperationOptions, OperationOptions

if TYPE_CHECKING:
    import aws_sdk_iam.types.delete_service_specific_credential_request


def delete_service_specific_credential(
    options: OperationOptions,
    input: aws_sdk_iam.types.delete_service_specific_credential_request.DeleteServiceSpecificCredentialRequest,
) -> tuple[None, zapros.Response]:
    raise NotImplementedError("operation dispatch not yet generated")


async def async_delete_service_specific_credential(
    options: AsyncOperationOptions,
    input: aws_sdk_iam.types.delete_service_specific_credential_request.DeleteServiceSpecificCredentialRequest,
) -> tuple[None, zapros.Response]:
    raise NotImplementedError("operation dispatch not yet generated")
