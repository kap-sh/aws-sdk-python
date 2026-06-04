"""Generated from Smithy shape ``com.amazonaws.iam#ListServerCertificates``."""

from __future__ import annotations
from typing import TYPE_CHECKING
import zapros
import aws_sdk_iam._auth._signers
from aws_sdk_iam._services._pipeline import AsyncOperationOptions, OperationOptions

if TYPE_CHECKING:
    import aws_sdk_iam.types.list_server_certificates_request
    import aws_sdk_iam.types.list_server_certificates_response


def list_server_certificates(
    options: OperationOptions,
    input: aws_sdk_iam.types.list_server_certificates_request.ListServerCertificatesRequest,
) -> tuple[
    aws_sdk_iam.types.list_server_certificates_response.ListServerCertificatesResponse,
    zapros.Response,
]:
    raise NotImplementedError("operation dispatch not yet generated")


async def async_list_server_certificates(
    options: AsyncOperationOptions,
    input: aws_sdk_iam.types.list_server_certificates_request.ListServerCertificatesRequest,
) -> tuple[
    aws_sdk_iam.types.list_server_certificates_response.ListServerCertificatesResponse,
    zapros.Response,
]:
    raise NotImplementedError("operation dispatch not yet generated")
