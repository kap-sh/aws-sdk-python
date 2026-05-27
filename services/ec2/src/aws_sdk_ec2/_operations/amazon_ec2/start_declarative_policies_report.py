"""Generated from Smithy shape ``com.amazonaws.ec2#StartDeclarativePoliciesReport``."""

from __future__ import annotations
from typing import TYPE_CHECKING
import zapros
import aws_sdk_ec2._auth._signers
from aws_sdk_ec2._services._pipeline import AsyncOperationOptions, OperationOptions

if TYPE_CHECKING:
    import aws_sdk_ec2.types.start_declarative_policies_report_request
    import aws_sdk_ec2.types.start_declarative_policies_report_result


def start_declarative_policies_report(
    options: OperationOptions,
    input: aws_sdk_ec2.types.start_declarative_policies_report_request.StartDeclarativePoliciesReportRequest,
) -> tuple[
    aws_sdk_ec2.types.start_declarative_policies_report_result.StartDeclarativePoliciesReportResult,
    zapros.Response,
]:
    raise NotImplementedError("operation dispatch not yet generated")


async def async_start_declarative_policies_report(
    options: AsyncOperationOptions,
    input: aws_sdk_ec2.types.start_declarative_policies_report_request.StartDeclarativePoliciesReportRequest,
) -> tuple[
    aws_sdk_ec2.types.start_declarative_policies_report_result.StartDeclarativePoliciesReportResult,
    zapros.Response,
]:
    raise NotImplementedError("operation dispatch not yet generated")
