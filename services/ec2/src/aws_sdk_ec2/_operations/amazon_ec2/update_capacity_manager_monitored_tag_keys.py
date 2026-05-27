"""Generated from Smithy shape ``com.amazonaws.ec2#UpdateCapacityManagerMonitoredTagKeys``."""

from __future__ import annotations
from typing import TYPE_CHECKING
import zapros
import aws_sdk_ec2._auth._signers
from aws_sdk_ec2._services._pipeline import AsyncOperationOptions, OperationOptions

if TYPE_CHECKING:
    import aws_sdk_ec2.types.update_capacity_manager_monitored_tag_keys_request
    import aws_sdk_ec2.types.update_capacity_manager_monitored_tag_keys_result


def update_capacity_manager_monitored_tag_keys(
    options: OperationOptions,
    input: aws_sdk_ec2.types.update_capacity_manager_monitored_tag_keys_request.UpdateCapacityManagerMonitoredTagKeysRequest,
) -> tuple[
    aws_sdk_ec2.types.update_capacity_manager_monitored_tag_keys_result.UpdateCapacityManagerMonitoredTagKeysResult,
    zapros.Response,
]:
    raise NotImplementedError("operation dispatch not yet generated")


async def async_update_capacity_manager_monitored_tag_keys(
    options: AsyncOperationOptions,
    input: aws_sdk_ec2.types.update_capacity_manager_monitored_tag_keys_request.UpdateCapacityManagerMonitoredTagKeysRequest,
) -> tuple[
    aws_sdk_ec2.types.update_capacity_manager_monitored_tag_keys_result.UpdateCapacityManagerMonitoredTagKeysResult,
    zapros.Response,
]:
    raise NotImplementedError("operation dispatch not yet generated")
