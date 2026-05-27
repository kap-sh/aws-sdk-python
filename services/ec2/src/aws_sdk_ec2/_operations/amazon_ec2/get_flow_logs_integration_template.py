"""Generated from Smithy shape ``com.amazonaws.ec2#GetFlowLogsIntegrationTemplate``."""

from __future__ import annotations
from typing import TYPE_CHECKING
import zapros
import aws_sdk_ec2._auth._signers
from aws_sdk_ec2._services._pipeline import AsyncOperationOptions, OperationOptions

if TYPE_CHECKING:
    import aws_sdk_ec2.types.get_flow_logs_integration_template_request
    import aws_sdk_ec2.types.get_flow_logs_integration_template_result


def get_flow_logs_integration_template(
    options: OperationOptions,
    input: aws_sdk_ec2.types.get_flow_logs_integration_template_request.GetFlowLogsIntegrationTemplateRequest,
) -> tuple[
    aws_sdk_ec2.types.get_flow_logs_integration_template_result.GetFlowLogsIntegrationTemplateResult,
    zapros.Response,
]:
    raise NotImplementedError("operation dispatch not yet generated")


async def async_get_flow_logs_integration_template(
    options: AsyncOperationOptions,
    input: aws_sdk_ec2.types.get_flow_logs_integration_template_request.GetFlowLogsIntegrationTemplateRequest,
) -> tuple[
    aws_sdk_ec2.types.get_flow_logs_integration_template_result.GetFlowLogsIntegrationTemplateResult,
    zapros.Response,
]:
    raise NotImplementedError("operation dispatch not yet generated")
