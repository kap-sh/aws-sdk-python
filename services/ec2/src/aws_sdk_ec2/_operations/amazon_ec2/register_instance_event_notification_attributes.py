"""Generated from Smithy shape ``com.amazonaws.ec2#RegisterInstanceEventNotificationAttributes``."""

from __future__ import annotations
from typing import TYPE_CHECKING
import zapros
import aws_sdk_ec2._auth._signers
from aws_sdk_ec2._services._pipeline import AsyncOperationOptions, OperationOptions

if TYPE_CHECKING:
    import aws_sdk_ec2.types.register_instance_event_notification_attributes_request
    import aws_sdk_ec2.types.register_instance_event_notification_attributes_result


def register_instance_event_notification_attributes(
    options: OperationOptions,
    input: aws_sdk_ec2.types.register_instance_event_notification_attributes_request.RegisterInstanceEventNotificationAttributesRequest,
) -> tuple[
    aws_sdk_ec2.types.register_instance_event_notification_attributes_result.RegisterInstanceEventNotificationAttributesResult,
    zapros.Response,
]:
    raise NotImplementedError("operation dispatch not yet generated")


async def async_register_instance_event_notification_attributes(
    options: AsyncOperationOptions,
    input: aws_sdk_ec2.types.register_instance_event_notification_attributes_request.RegisterInstanceEventNotificationAttributesRequest,
) -> tuple[
    aws_sdk_ec2.types.register_instance_event_notification_attributes_result.RegisterInstanceEventNotificationAttributesResult,
    zapros.Response,
]:
    raise NotImplementedError("operation dispatch not yet generated")
