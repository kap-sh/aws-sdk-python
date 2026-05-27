"""Generated from Smithy shape ``com.amazonaws.ec2#UnmonitorInstances``."""

from __future__ import annotations
from typing import TYPE_CHECKING
import zapros
import aws_sdk_ec2._auth._signers
from aws_sdk_ec2._services._pipeline import AsyncOperationOptions, OperationOptions

if TYPE_CHECKING:
    import aws_sdk_ec2.types.unmonitor_instances_request
    import aws_sdk_ec2.types.unmonitor_instances_result


def unmonitor_instances(
    options: OperationOptions,
    input: aws_sdk_ec2.types.unmonitor_instances_request.UnmonitorInstancesRequest,
) -> tuple[
    aws_sdk_ec2.types.unmonitor_instances_result.UnmonitorInstancesResult,
    zapros.Response,
]:
    raise NotImplementedError("operation dispatch not yet generated")


async def async_unmonitor_instances(
    options: AsyncOperationOptions,
    input: aws_sdk_ec2.types.unmonitor_instances_request.UnmonitorInstancesRequest,
) -> tuple[
    aws_sdk_ec2.types.unmonitor_instances_result.UnmonitorInstancesResult,
    zapros.Response,
]:
    raise NotImplementedError("operation dispatch not yet generated")
