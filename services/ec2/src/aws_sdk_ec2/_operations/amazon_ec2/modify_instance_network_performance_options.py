"""Generated from Smithy shape ``com.amazonaws.ec2#ModifyInstanceNetworkPerformanceOptions``."""

from __future__ import annotations
from typing import TYPE_CHECKING
import zapros
import aws_sdk_ec2._auth._signers
from aws_sdk_ec2._services._pipeline import AsyncOperationOptions, OperationOptions

if TYPE_CHECKING:
    import aws_sdk_ec2.types.modify_instance_network_performance_request
    import aws_sdk_ec2.types.modify_instance_network_performance_result


def modify_instance_network_performance_options(
    options: OperationOptions,
    input: aws_sdk_ec2.types.modify_instance_network_performance_request.ModifyInstanceNetworkPerformanceRequest,
) -> tuple[
    aws_sdk_ec2.types.modify_instance_network_performance_result.ModifyInstanceNetworkPerformanceResult,
    zapros.Response,
]:
    raise NotImplementedError("operation dispatch not yet generated")


async def async_modify_instance_network_performance_options(
    options: AsyncOperationOptions,
    input: aws_sdk_ec2.types.modify_instance_network_performance_request.ModifyInstanceNetworkPerformanceRequest,
) -> tuple[
    aws_sdk_ec2.types.modify_instance_network_performance_result.ModifyInstanceNetworkPerformanceResult,
    zapros.Response,
]:
    raise NotImplementedError("operation dispatch not yet generated")
