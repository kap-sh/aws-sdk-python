"""Generated from Smithy shape ``com.amazonaws.ec2#DeleteLaunchTemplate``."""

from __future__ import annotations
from typing import TYPE_CHECKING
import zapros
import aws_sdk_ec2._auth._signers
from aws_sdk_ec2._services._pipeline import AsyncOperationOptions, OperationOptions

if TYPE_CHECKING:
    import aws_sdk_ec2.types.delete_launch_template_request
    import aws_sdk_ec2.types.delete_launch_template_result


def delete_launch_template(
    options: OperationOptions,
    input: aws_sdk_ec2.types.delete_launch_template_request.DeleteLaunchTemplateRequest,
) -> tuple[
    aws_sdk_ec2.types.delete_launch_template_result.DeleteLaunchTemplateResult,
    zapros.Response,
]:
    raise NotImplementedError("operation dispatch not yet generated")


async def async_delete_launch_template(
    options: AsyncOperationOptions,
    input: aws_sdk_ec2.types.delete_launch_template_request.DeleteLaunchTemplateRequest,
) -> tuple[
    aws_sdk_ec2.types.delete_launch_template_result.DeleteLaunchTemplateResult,
    zapros.Response,
]:
    raise NotImplementedError("operation dispatch not yet generated")
