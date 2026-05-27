"""Generated from Smithy shape ``com.amazonaws.ec2#MonitorInstances``."""

from __future__ import annotations
from typing import TYPE_CHECKING
import zapros
import aws_sdk_ec2._auth._signers
from aws_sdk_ec2._services._pipeline import AsyncOperationOptions, OperationOptions

if TYPE_CHECKING:
    import aws_sdk_ec2.types.monitor_instances_request
    import aws_sdk_ec2.types.monitor_instances_result


def monitor_instances(
    options: OperationOptions,
    input: aws_sdk_ec2.types.monitor_instances_request.MonitorInstancesRequest,
) -> tuple[
    aws_sdk_ec2.types.monitor_instances_result.MonitorInstancesResult, zapros.Response
]:
    raise NotImplementedError("operation dispatch not yet generated")


async def async_monitor_instances(
    options: AsyncOperationOptions,
    input: aws_sdk_ec2.types.monitor_instances_request.MonitorInstancesRequest,
) -> tuple[
    aws_sdk_ec2.types.monitor_instances_result.MonitorInstancesResult, zapros.Response
]:
    raise NotImplementedError("operation dispatch not yet generated")
