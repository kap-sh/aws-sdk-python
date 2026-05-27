"""Generated from Smithy shape ``com.amazonaws.ec2#StopInstances``."""

from __future__ import annotations
from typing import TYPE_CHECKING
import zapros
import aws_sdk_ec2._auth._signers
from aws_sdk_ec2._services._pipeline import AsyncOperationOptions, OperationOptions

if TYPE_CHECKING:
    import aws_sdk_ec2.types.stop_instances_request
    import aws_sdk_ec2.types.stop_instances_result


def stop_instances(
    options: OperationOptions,
    input: aws_sdk_ec2.types.stop_instances_request.StopInstancesRequest,
) -> tuple[
    aws_sdk_ec2.types.stop_instances_result.StopInstancesResult, zapros.Response
]:
    raise NotImplementedError("operation dispatch not yet generated")


async def async_stop_instances(
    options: AsyncOperationOptions,
    input: aws_sdk_ec2.types.stop_instances_request.StopInstancesRequest,
) -> tuple[
    aws_sdk_ec2.types.stop_instances_result.StopInstancesResult, zapros.Response
]:
    raise NotImplementedError("operation dispatch not yet generated")
