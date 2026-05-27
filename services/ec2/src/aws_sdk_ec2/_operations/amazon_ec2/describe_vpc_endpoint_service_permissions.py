"""Generated from Smithy shape ``com.amazonaws.ec2#DescribeVpcEndpointServicePermissions``."""

from __future__ import annotations
from typing import TYPE_CHECKING
import zapros
import aws_sdk_ec2._auth._signers
from aws_sdk_ec2._services._pipeline import AsyncOperationOptions, OperationOptions

if TYPE_CHECKING:
    import aws_sdk_ec2.types.describe_vpc_endpoint_service_permissions_request
    import aws_sdk_ec2.types.describe_vpc_endpoint_service_permissions_result


def describe_vpc_endpoint_service_permissions(
    options: OperationOptions,
    input: aws_sdk_ec2.types.describe_vpc_endpoint_service_permissions_request.DescribeVpcEndpointServicePermissionsRequest,
) -> tuple[
    aws_sdk_ec2.types.describe_vpc_endpoint_service_permissions_result.DescribeVpcEndpointServicePermissionsResult,
    zapros.Response,
]:
    raise NotImplementedError("operation dispatch not yet generated")


async def async_describe_vpc_endpoint_service_permissions(
    options: AsyncOperationOptions,
    input: aws_sdk_ec2.types.describe_vpc_endpoint_service_permissions_request.DescribeVpcEndpointServicePermissionsRequest,
) -> tuple[
    aws_sdk_ec2.types.describe_vpc_endpoint_service_permissions_result.DescribeVpcEndpointServicePermissionsResult,
    zapros.Response,
]:
    raise NotImplementedError("operation dispatch not yet generated")
