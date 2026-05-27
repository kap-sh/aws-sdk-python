"""Generated from Smithy shape ``com.amazonaws.ec2#ModifyVpcEndpointConnectionNotification``."""

from __future__ import annotations
from typing import TYPE_CHECKING
import zapros
import aws_sdk_ec2._auth._signers
from aws_sdk_ec2._services._pipeline import AsyncOperationOptions, OperationOptions

if TYPE_CHECKING:
    import aws_sdk_ec2.types.modify_vpc_endpoint_connection_notification_request
    import aws_sdk_ec2.types.modify_vpc_endpoint_connection_notification_result


def modify_vpc_endpoint_connection_notification(
    options: OperationOptions,
    input: aws_sdk_ec2.types.modify_vpc_endpoint_connection_notification_request.ModifyVpcEndpointConnectionNotificationRequest,
) -> tuple[
    aws_sdk_ec2.types.modify_vpc_endpoint_connection_notification_result.ModifyVpcEndpointConnectionNotificationResult,
    zapros.Response,
]:
    raise NotImplementedError("operation dispatch not yet generated")


async def async_modify_vpc_endpoint_connection_notification(
    options: AsyncOperationOptions,
    input: aws_sdk_ec2.types.modify_vpc_endpoint_connection_notification_request.ModifyVpcEndpointConnectionNotificationRequest,
) -> tuple[
    aws_sdk_ec2.types.modify_vpc_endpoint_connection_notification_result.ModifyVpcEndpointConnectionNotificationResult,
    zapros.Response,
]:
    raise NotImplementedError("operation dispatch not yet generated")
