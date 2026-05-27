"""Generated from Smithy shape ``com.amazonaws.ec2#GetCapacityManagerMonitoredTagKeys``."""

from __future__ import annotations
from typing import TYPE_CHECKING
import zapros
import aws_sdk_ec2._auth._signers
from aws_sdk_ec2._services._pipeline import AsyncOperationOptions, OperationOptions

if TYPE_CHECKING:
    import aws_sdk_ec2.types.get_capacity_manager_monitored_tag_keys_request
    import aws_sdk_ec2.types.get_capacity_manager_monitored_tag_keys_result


def get_capacity_manager_monitored_tag_keys(
    options: OperationOptions,
    input: aws_sdk_ec2.types.get_capacity_manager_monitored_tag_keys_request.GetCapacityManagerMonitoredTagKeysRequest,
) -> tuple[
    aws_sdk_ec2.types.get_capacity_manager_monitored_tag_keys_result.GetCapacityManagerMonitoredTagKeysResult,
    zapros.Response,
]:
    raise NotImplementedError("operation dispatch not yet generated")


async def async_get_capacity_manager_monitored_tag_keys(
    options: AsyncOperationOptions,
    input: aws_sdk_ec2.types.get_capacity_manager_monitored_tag_keys_request.GetCapacityManagerMonitoredTagKeysRequest,
) -> tuple[
    aws_sdk_ec2.types.get_capacity_manager_monitored_tag_keys_result.GetCapacityManagerMonitoredTagKeysResult,
    zapros.Response,
]:
    raise NotImplementedError("operation dispatch not yet generated")
