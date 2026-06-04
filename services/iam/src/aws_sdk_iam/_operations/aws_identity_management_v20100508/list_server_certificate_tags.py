"""Generated from Smithy shape ``com.amazonaws.iam#ListServerCertificateTags``."""

from __future__ import annotations
from typing import TYPE_CHECKING
import zapros
import aws_sdk_iam._auth._signers
from aws_sdk_iam._services._pipeline import AsyncOperationOptions, OperationOptions

if TYPE_CHECKING:
    import aws_sdk_iam.types.list_server_certificate_tags_request
    import aws_sdk_iam.types.list_server_certificate_tags_response


def list_server_certificate_tags(
    options: OperationOptions,
    input: aws_sdk_iam.types.list_server_certificate_tags_request.ListServerCertificateTagsRequest,
) -> tuple[
    aws_sdk_iam.types.list_server_certificate_tags_response.ListServerCertificateTagsResponse,
    zapros.Response,
]:
    raise NotImplementedError("operation dispatch not yet generated")


async def async_list_server_certificate_tags(
    options: AsyncOperationOptions,
    input: aws_sdk_iam.types.list_server_certificate_tags_request.ListServerCertificateTagsRequest,
) -> tuple[
    aws_sdk_iam.types.list_server_certificate_tags_response.ListServerCertificateTagsResponse,
    zapros.Response,
]:
    raise NotImplementedError("operation dispatch not yet generated")
