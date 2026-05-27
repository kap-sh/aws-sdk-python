"""Generated from Smithy shape ``com.amazonaws.ec2#GetDeclarativePoliciesReportSummary``."""

from __future__ import annotations
from typing import TYPE_CHECKING
import zapros
import aws_sdk_ec2._auth._signers
from aws_sdk_ec2._services._pipeline import AsyncOperationOptions, OperationOptions

if TYPE_CHECKING:
    import aws_sdk_ec2.types.get_declarative_policies_report_summary_request
    import aws_sdk_ec2.types.get_declarative_policies_report_summary_result


def get_declarative_policies_report_summary(
    options: OperationOptions,
    input: aws_sdk_ec2.types.get_declarative_policies_report_summary_request.GetDeclarativePoliciesReportSummaryRequest,
) -> tuple[
    aws_sdk_ec2.types.get_declarative_policies_report_summary_result.GetDeclarativePoliciesReportSummaryResult,
    zapros.Response,
]:
    raise NotImplementedError("operation dispatch not yet generated")


async def async_get_declarative_policies_report_summary(
    options: AsyncOperationOptions,
    input: aws_sdk_ec2.types.get_declarative_policies_report_summary_request.GetDeclarativePoliciesReportSummaryRequest,
) -> tuple[
    aws_sdk_ec2.types.get_declarative_policies_report_summary_result.GetDeclarativePoliciesReportSummaryResult,
    zapros.Response,
]:
    raise NotImplementedError("operation dispatch not yet generated")
