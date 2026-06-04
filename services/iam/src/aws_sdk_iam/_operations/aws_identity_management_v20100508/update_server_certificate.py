"""Generated from Smithy shape ``com.amazonaws.iam#UpdateServerCertificate``."""

from __future__ import annotations
from typing import TYPE_CHECKING
import zapros
import aws_sdk_iam._auth._signers
from aws_sdk_iam._services._pipeline import AsyncOperationOptions, OperationOptions

if TYPE_CHECKING:
    import aws_sdk_iam.types.update_server_certificate_request


def update_server_certificate(
    options: OperationOptions,
    input: aws_sdk_iam.types.update_server_certificate_request.UpdateServerCertificateRequest,
) -> tuple[None, zapros.Response]:
    raise NotImplementedError("operation dispatch not yet generated")


async def async_update_server_certificate(
    options: AsyncOperationOptions,
    input: aws_sdk_iam.types.update_server_certificate_request.UpdateServerCertificateRequest,
) -> tuple[None, zapros.Response]:
    raise NotImplementedError("operation dispatch not yet generated")
