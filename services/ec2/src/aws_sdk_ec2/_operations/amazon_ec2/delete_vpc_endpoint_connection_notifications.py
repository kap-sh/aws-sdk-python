"""Generated from Smithy shape ``com.amazonaws.ec2#DeleteVpcEndpointConnectionNotifications``."""

from __future__ import annotations
from typing import TYPE_CHECKING
import zapros
import aws_sdk_ec2._auth._signers
from aws_sdk_ec2._services._pipeline import AsyncOperationOptions, OperationOptions

if TYPE_CHECKING:
    import aws_sdk_ec2.types.delete_vpc_endpoint_connection_notifications_request
    import aws_sdk_ec2.types.delete_vpc_endpoint_connection_notifications_result


def delete_vpc_endpoint_connection_notifications(
    options: OperationOptions,
    input: aws_sdk_ec2.types.delete_vpc_endpoint_connection_notifications_request.DeleteVpcEndpointConnectionNotificationsRequest,
) -> tuple[
    aws_sdk_ec2.types.delete_vpc_endpoint_connection_notifications_result.DeleteVpcEndpointConnectionNotificationsResult,
    zapros.Response,
]:
    raise NotImplementedError("operation dispatch not yet generated")


async def async_delete_vpc_endpoint_connection_notifications(
    options: AsyncOperationOptions,
    input: aws_sdk_ec2.types.delete_vpc_endpoint_connection_notifications_request.DeleteVpcEndpointConnectionNotificationsRequest,
) -> tuple[
    aws_sdk_ec2.types.delete_vpc_endpoint_connection_notifications_result.DeleteVpcEndpointConnectionNotificationsResult,
    zapros.Response,
]:
    raise NotImplementedError("operation dispatch not yet generated")
