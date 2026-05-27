"""Generated from Smithy shape ``com.amazonaws.ec2#EnableCapacityManager``."""

from __future__ import annotations
from typing import TYPE_CHECKING
import zapros
import aws_sdk_ec2._auth._signers
from aws_sdk_ec2._services._pipeline import AsyncOperationOptions, OperationOptions

if TYPE_CHECKING:
    import aws_sdk_ec2.types.enable_capacity_manager_request
    import aws_sdk_ec2.types.enable_capacity_manager_result


def enable_capacity_manager(
    options: OperationOptions,
    input: aws_sdk_ec2.types.enable_capacity_manager_request.EnableCapacityManagerRequest,
) -> tuple[
    aws_sdk_ec2.types.enable_capacity_manager_result.EnableCapacityManagerResult,
    zapros.Response,
]:
    raise NotImplementedError("operation dispatch not yet generated")


async def async_enable_capacity_manager(
    options: AsyncOperationOptions,
    input: aws_sdk_ec2.types.enable_capacity_manager_request.EnableCapacityManagerRequest,
) -> tuple[
    aws_sdk_ec2.types.enable_capacity_manager_result.EnableCapacityManagerResult,
    zapros.Response,
]:
    raise NotImplementedError("operation dispatch not yet generated")
