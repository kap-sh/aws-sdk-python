"""Generated from Smithy shape ``com.amazonaws.iam#DeleteSigningCertificate``."""

from __future__ import annotations
from typing import TYPE_CHECKING
import zapros
import aws_sdk_iam._auth._signers
from aws_sdk_iam._services._pipeline import AsyncOperationOptions, OperationOptions

if TYPE_CHECKING:
    import aws_sdk_iam.types.delete_signing_certificate_request


def delete_signing_certificate(
    options: OperationOptions,
    input: aws_sdk_iam.types.delete_signing_certificate_request.DeleteSigningCertificateRequest,
) -> tuple[None, zapros.Response]:
    raise NotImplementedError("operation dispatch not yet generated")


async def async_delete_signing_certificate(
    options: AsyncOperationOptions,
    input: aws_sdk_iam.types.delete_signing_certificate_request.DeleteSigningCertificateRequest,
) -> tuple[None, zapros.Response]:
    raise NotImplementedError("operation dispatch not yet generated")
