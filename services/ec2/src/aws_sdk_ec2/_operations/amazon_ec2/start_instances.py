"""Generated from Smithy shape ``com.amazonaws.ec2#StartInstances``."""

from __future__ import annotations
from typing import TYPE_CHECKING
import zapros
import aws_sdk_ec2._auth._signers
from aws_sdk_ec2._services._pipeline import AsyncOperationOptions, OperationOptions

if TYPE_CHECKING:
    import aws_sdk_ec2.types.start_instances_request
    import aws_sdk_ec2.types.start_instances_result


def start_instances(
    options: OperationOptions,
    input: aws_sdk_ec2.types.start_instances_request.StartInstancesRequest,
) -> tuple[
    aws_sdk_ec2.types.start_instances_result.StartInstancesResult, zapros.Response
]:
    raise NotImplementedError("operation dispatch not yet generated")


async def async_start_instances(
    options: AsyncOperationOptions,
    input: aws_sdk_ec2.types.start_instances_request.StartInstancesRequest,
) -> tuple[
    aws_sdk_ec2.types.start_instances_result.StartInstancesResult, zapros.Response
]:
    raise NotImplementedError("operation dispatch not yet generated")
