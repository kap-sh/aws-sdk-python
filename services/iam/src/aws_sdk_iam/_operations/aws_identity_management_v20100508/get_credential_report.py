"""Generated from Smithy shape ``com.amazonaws.iam#GetCredentialReport``."""

from __future__ import annotations
from typing import TYPE_CHECKING
import zapros
import aws_sdk_iam._auth._signers
from aws_sdk_iam._services._pipeline import AsyncOperationOptions, OperationOptions

if TYPE_CHECKING:
    import aws_sdk_iam.types.get_credential_report_response


def get_credential_report(
    options: OperationOptions,
) -> tuple[
    aws_sdk_iam.types.get_credential_report_response.GetCredentialReportResponse,
    zapros.Response,
]:
    raise NotImplementedError("operation dispatch not yet generated")


async def async_get_credential_report(
    options: AsyncOperationOptions,
) -> tuple[
    aws_sdk_iam.types.get_credential_report_response.GetCredentialReportResponse,
    zapros.Response,
]:
    raise NotImplementedError("operation dispatch not yet generated")
