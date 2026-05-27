"""Generated from Smithy shape ``com.amazonaws.ec2#RunScheduledInstances``."""

from __future__ import annotations
from typing import TYPE_CHECKING
import zapros
import aws_sdk_ec2._auth._signers
from aws_sdk_ec2._services._pipeline import AsyncOperationOptions, OperationOptions

if TYPE_CHECKING:
    import aws_sdk_ec2.types.run_scheduled_instances_request
    import aws_sdk_ec2.types.run_scheduled_instances_result


def run_scheduled_instances(
    options: OperationOptions,
    input: aws_sdk_ec2.types.run_scheduled_instances_request.RunScheduledInstancesRequest,
) -> tuple[
    aws_sdk_ec2.types.run_scheduled_instances_result.RunScheduledInstancesResult,
    zapros.Response,
]:
    raise NotImplementedError("operation dispatch not yet generated")


async def async_run_scheduled_instances(
    options: AsyncOperationOptions,
    input: aws_sdk_ec2.types.run_scheduled_instances_request.RunScheduledInstancesRequest,
) -> tuple[
    aws_sdk_ec2.types.run_scheduled_instances_result.RunScheduledInstancesResult,
    zapros.Response,
]:
    raise NotImplementedError("operation dispatch not yet generated")
