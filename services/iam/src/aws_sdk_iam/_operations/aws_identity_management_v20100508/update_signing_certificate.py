"""Generated from Smithy shape ``com.amazonaws.iam#UpdateSigningCertificate``."""

from __future__ import annotations
from typing import TYPE_CHECKING
import zapros
import aws_sdk_iam._auth._signers
from aws_sdk_iam._services._pipeline import AsyncOperationOptions, OperationOptions

if TYPE_CHECKING:
    import aws_sdk_iam.types.update_signing_certificate_request


def update_signing_certificate(
    options: OperationOptions,
    input: aws_sdk_iam.types.update_signing_certificate_request.UpdateSigningCertificateRequest,
) -> tuple[None, zapros.Response]:
    raise NotImplementedError("operation dispatch not yet generated")


async def async_update_signing_certificate(
    options: AsyncOperationOptions,
    input: aws_sdk_iam.types.update_signing_certificate_request.UpdateSigningCertificateRequest,
) -> tuple[None, zapros.Response]:
    raise NotImplementedError("operation dispatch not yet generated")
