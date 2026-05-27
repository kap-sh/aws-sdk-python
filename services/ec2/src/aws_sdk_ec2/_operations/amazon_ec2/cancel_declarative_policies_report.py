"""Generated from Smithy shape ``com.amazonaws.ec2#CancelDeclarativePoliciesReport``."""

from __future__ import annotations
from typing import TYPE_CHECKING
import zapros
import aws_sdk_ec2._auth._signers
from aws_sdk_ec2._services._pipeline import AsyncOperationOptions, OperationOptions

if TYPE_CHECKING:
    import aws_sdk_ec2.types.cancel_declarative_policies_report_request
    import aws_sdk_ec2.types.cancel_declarative_policies_report_result


def cancel_declarative_policies_report(
    options: OperationOptions,
    input: aws_sdk_ec2.types.cancel_declarative_policies_report_request.CancelDeclarativePoliciesReportRequest,
) -> tuple[
    aws_sdk_ec2.types.cancel_declarative_policies_report_result.CancelDeclarativePoliciesReportResult,
    zapros.Response,
]:
    raise NotImplementedError("operation dispatch not yet generated")


async def async_cancel_declarative_policies_report(
    options: AsyncOperationOptions,
    input: aws_sdk_ec2.types.cancel_declarative_policies_report_request.CancelDeclarativePoliciesReportRequest,
) -> tuple[
    aws_sdk_ec2.types.cancel_declarative_policies_report_result.CancelDeclarativePoliciesReportResult,
    zapros.Response,
]:
    raise NotImplementedError("operation dispatch not yet generated")
