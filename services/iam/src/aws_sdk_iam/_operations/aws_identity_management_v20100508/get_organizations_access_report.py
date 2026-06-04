"""Generated from Smithy shape ``com.amazonaws.iam#GetOrganizationsAccessReport``."""

from __future__ import annotations
from typing import TYPE_CHECKING
import zapros
import aws_sdk_iam._auth._signers
from aws_sdk_iam._services._pipeline import AsyncOperationOptions, OperationOptions

if TYPE_CHECKING:
    import aws_sdk_iam.types.get_organizations_access_report_request
    import aws_sdk_iam.types.get_organizations_access_report_response


def get_organizations_access_report(
    options: OperationOptions,
    input: aws_sdk_iam.types.get_organizations_access_report_request.GetOrganizationsAccessReportRequest,
) -> tuple[
    aws_sdk_iam.types.get_organizations_access_report_response.GetOrganizationsAccessReportResponse,
    zapros.Response,
]:
    raise NotImplementedError("operation dispatch not yet generated")


async def async_get_organizations_access_report(
    options: AsyncOperationOptions,
    input: aws_sdk_iam.types.get_organizations_access_report_request.GetOrganizationsAccessReportRequest,
) -> tuple[
    aws_sdk_iam.types.get_organizations_access_report_response.GetOrganizationsAccessReportResponse,
    zapros.Response,
]:
    raise NotImplementedError("operation dispatch not yet generated")
