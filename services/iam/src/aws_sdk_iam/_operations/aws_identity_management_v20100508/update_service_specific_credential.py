"""Generated from Smithy shape ``com.amazonaws.iam#UpdateServiceSpecificCredential``."""

from __future__ import annotations
from typing import TYPE_CHECKING
import zapros
import aws_sdk_iam._auth._signers
from aws_sdk_iam._services._pipeline import AsyncOperationOptions, OperationOptions

if TYPE_CHECKING:
    import aws_sdk_iam.types.update_service_specific_credential_request


def update_service_specific_credential(
    options: OperationOptions,
    input: aws_sdk_iam.types.update_service_specific_credential_request.UpdateServiceSpecificCredentialRequest,
) -> tuple[None, zapros.Response]:
    raise NotImplementedError("operation dispatch not yet generated")


async def async_update_service_specific_credential(
    options: AsyncOperationOptions,
    input: aws_sdk_iam.types.update_service_specific_credential_request.UpdateServiceSpecificCredentialRequest,
) -> tuple[None, zapros.Response]:
    raise NotImplementedError("operation dispatch not yet generated")
