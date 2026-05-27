"""Generated from Smithy shape ``com.amazonaws.ec2#DeleteLaunchTemplateVersions``."""

from __future__ import annotations
from typing import TYPE_CHECKING
import zapros
import aws_sdk_ec2._auth._signers
from aws_sdk_ec2._services._pipeline import AsyncOperationOptions, OperationOptions

if TYPE_CHECKING:
    import aws_sdk_ec2.types.delete_launch_template_versions_request
    import aws_sdk_ec2.types.delete_launch_template_versions_result


def delete_launch_template_versions(
    options: OperationOptions,
    input: aws_sdk_ec2.types.delete_launch_template_versions_request.DeleteLaunchTemplateVersionsRequest,
) -> tuple[
    aws_sdk_ec2.types.delete_launch_template_versions_result.DeleteLaunchTemplateVersionsResult,
    zapros.Response,
]:
    raise NotImplementedError("operation dispatch not yet generated")


async def async_delete_launch_template_versions(
    options: AsyncOperationOptions,
    input: aws_sdk_ec2.types.delete_launch_template_versions_request.DeleteLaunchTemplateVersionsRequest,
) -> tuple[
    aws_sdk_ec2.types.delete_launch_template_versions_result.DeleteLaunchTemplateVersionsResult,
    zapros.Response,
]:
    raise NotImplementedError("operation dispatch not yet generated")
