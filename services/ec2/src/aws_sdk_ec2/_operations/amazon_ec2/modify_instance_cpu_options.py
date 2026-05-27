"""Generated from Smithy shape ``com.amazonaws.ec2#ModifyInstanceCpuOptions``."""

from __future__ import annotations
from typing import TYPE_CHECKING
import zapros
import aws_sdk_ec2._auth._signers
from aws_sdk_ec2._services._pipeline import AsyncOperationOptions, OperationOptions

if TYPE_CHECKING:
    import aws_sdk_ec2.types.modify_instance_cpu_options_request
    import aws_sdk_ec2.types.modify_instance_cpu_options_result


def modify_instance_cpu_options(
    options: OperationOptions,
    input: aws_sdk_ec2.types.modify_instance_cpu_options_request.ModifyInstanceCpuOptionsRequest,
) -> tuple[
    aws_sdk_ec2.types.modify_instance_cpu_options_result.ModifyInstanceCpuOptionsResult,
    zapros.Response,
]:
    raise NotImplementedError("operation dispatch not yet generated")


async def async_modify_instance_cpu_options(
    options: AsyncOperationOptions,
    input: aws_sdk_ec2.types.modify_instance_cpu_options_request.ModifyInstanceCpuOptionsRequest,
) -> tuple[
    aws_sdk_ec2.types.modify_instance_cpu_options_result.ModifyInstanceCpuOptionsResult,
    zapros.Response,
]:
    raise NotImplementedError("operation dispatch not yet generated")
