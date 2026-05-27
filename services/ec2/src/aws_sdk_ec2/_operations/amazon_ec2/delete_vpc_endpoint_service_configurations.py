"""Generated from Smithy shape ``com.amazonaws.ec2#DeleteVpcEndpointServiceConfigurations``."""

from __future__ import annotations
from typing import TYPE_CHECKING
import zapros
import aws_sdk_ec2._auth._signers
from aws_sdk_ec2._services._pipeline import AsyncOperationOptions, OperationOptions

if TYPE_CHECKING:
    import aws_sdk_ec2.types.delete_vpc_endpoint_service_configurations_request
    import aws_sdk_ec2.types.delete_vpc_endpoint_service_configurations_result


def delete_vpc_endpoint_service_configurations(
    options: OperationOptions,
    input: aws_sdk_ec2.types.delete_vpc_endpoint_service_configurations_request.DeleteVpcEndpointServiceConfigurationsRequest,
) -> tuple[
    aws_sdk_ec2.types.delete_vpc_endpoint_service_configurations_result.DeleteVpcEndpointServiceConfigurationsResult,
    zapros.Response,
]:
    raise NotImplementedError("operation dispatch not yet generated")


async def async_delete_vpc_endpoint_service_configurations(
    options: AsyncOperationOptions,
    input: aws_sdk_ec2.types.delete_vpc_endpoint_service_configurations_request.DeleteVpcEndpointServiceConfigurationsRequest,
) -> tuple[
    aws_sdk_ec2.types.delete_vpc_endpoint_service_configurations_result.DeleteVpcEndpointServiceConfigurationsResult,
    zapros.Response,
]:
    raise NotImplementedError("operation dispatch not yet generated")
