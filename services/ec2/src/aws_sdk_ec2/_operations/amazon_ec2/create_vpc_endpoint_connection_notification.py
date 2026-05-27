"""Generated from Smithy shape ``com.amazonaws.ec2#CreateVpcEndpointConnectionNotification``."""

from __future__ import annotations
from typing import TYPE_CHECKING
import zapros
import aws_sdk_ec2._auth._signers
from aws_sdk_ec2._services._pipeline import AsyncOperationOptions, OperationOptions

if TYPE_CHECKING:
    import aws_sdk_ec2.types.create_vpc_endpoint_connection_notification_request
    import aws_sdk_ec2.types.create_vpc_endpoint_connection_notification_result


def create_vpc_endpoint_connection_notification(
    options: OperationOptions,
    input: aws_sdk_ec2.types.create_vpc_endpoint_connection_notification_request.CreateVpcEndpointConnectionNotificationRequest,
) -> tuple[
    aws_sdk_ec2.types.create_vpc_endpoint_connection_notification_result.CreateVpcEndpointConnectionNotificationResult,
    zapros.Response,
]:
    raise NotImplementedError("operation dispatch not yet generated")


async def async_create_vpc_endpoint_connection_notification(
    options: AsyncOperationOptions,
    input: aws_sdk_ec2.types.create_vpc_endpoint_connection_notification_request.CreateVpcEndpointConnectionNotificationRequest,
) -> tuple[
    aws_sdk_ec2.types.create_vpc_endpoint_connection_notification_result.CreateVpcEndpointConnectionNotificationResult,
    zapros.Response,
]:
    raise NotImplementedError("operation dispatch not yet generated")
