"""Generated from Smithy shape ``com.amazonaws.ec2#ModifyManagedResourceVisibility``."""

from __future__ import annotations
from typing import TYPE_CHECKING
import zapros
import aws_sdk_ec2._auth._signers
from aws_sdk_ec2._services._pipeline import AsyncOperationOptions, OperationOptions

if TYPE_CHECKING:
    import aws_sdk_ec2.types.modify_managed_resource_visibility_request
    import aws_sdk_ec2.types.modify_managed_resource_visibility_result


def modify_managed_resource_visibility(
    options: OperationOptions,
    input: aws_sdk_ec2.types.modify_managed_resource_visibility_request.ModifyManagedResourceVisibilityRequest,
) -> tuple[
    aws_sdk_ec2.types.modify_managed_resource_visibility_result.ModifyManagedResourceVisibilityResult,
    zapros.Response,
]:
    raise NotImplementedError("operation dispatch not yet generated")


async def async_modify_managed_resource_visibility(
    options: AsyncOperationOptions,
    input: aws_sdk_ec2.types.modify_managed_resource_visibility_request.ModifyManagedResourceVisibilityRequest,
) -> tuple[
    aws_sdk_ec2.types.modify_managed_resource_visibility_result.ModifyManagedResourceVisibilityResult,
    zapros.Response,
]:
    raise NotImplementedError("operation dispatch not yet generated")
