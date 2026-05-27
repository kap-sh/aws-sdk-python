"""Generated from Smithy shape ``com.amazonaws.ec2#GetLaunchTemplateData``."""

from __future__ import annotations
from typing import TYPE_CHECKING
import zapros
import aws_sdk_ec2._auth._signers
from aws_sdk_ec2._services._pipeline import AsyncOperationOptions, OperationOptions

if TYPE_CHECKING:
    import aws_sdk_ec2.types.get_launch_template_data_request
    import aws_sdk_ec2.types.get_launch_template_data_result


def get_launch_template_data(
    options: OperationOptions,
    input: aws_sdk_ec2.types.get_launch_template_data_request.GetLaunchTemplateDataRequest,
) -> tuple[
    aws_sdk_ec2.types.get_launch_template_data_result.GetLaunchTemplateDataResult,
    zapros.Response,
]:
    raise NotImplementedError("operation dispatch not yet generated")


async def async_get_launch_template_data(
    options: AsyncOperationOptions,
    input: aws_sdk_ec2.types.get_launch_template_data_request.GetLaunchTemplateDataRequest,
) -> tuple[
    aws_sdk_ec2.types.get_launch_template_data_result.GetLaunchTemplateDataResult,
    zapros.Response,
]:
    raise NotImplementedError("operation dispatch not yet generated")
