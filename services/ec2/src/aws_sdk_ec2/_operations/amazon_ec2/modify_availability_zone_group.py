"""Generated from Smithy shape ``com.amazonaws.ec2#ModifyAvailabilityZoneGroup``."""

from __future__ import annotations
from typing import TYPE_CHECKING
import zapros
import aws_sdk_ec2._auth._signers
from aws_sdk_ec2._services._pipeline import AsyncOperationOptions, OperationOptions

if TYPE_CHECKING:
    import aws_sdk_ec2.types.modify_availability_zone_group_request
    import aws_sdk_ec2.types.modify_availability_zone_group_result


def modify_availability_zone_group(
    options: OperationOptions,
    input: aws_sdk_ec2.types.modify_availability_zone_group_request.ModifyAvailabilityZoneGroupRequest,
) -> tuple[
    aws_sdk_ec2.types.modify_availability_zone_group_result.ModifyAvailabilityZoneGroupResult,
    zapros.Response,
]:
    raise NotImplementedError("operation dispatch not yet generated")


async def async_modify_availability_zone_group(
    options: AsyncOperationOptions,
    input: aws_sdk_ec2.types.modify_availability_zone_group_request.ModifyAvailabilityZoneGroupRequest,
) -> tuple[
    aws_sdk_ec2.types.modify_availability_zone_group_result.ModifyAvailabilityZoneGroupResult,
    zapros.Response,
]:
    raise NotImplementedError("operation dispatch not yet generated")
