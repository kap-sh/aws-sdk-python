"""Generated from Smithy shape ``com.amazonaws.ec2#CreateVpcEndpointServiceConfiguration``."""

from __future__ import annotations
from typing import TYPE_CHECKING
import zapros
import aws_sdk_ec2._auth._signers
from aws_sdk_ec2._services._pipeline import AsyncOperationOptions, OperationOptions

if TYPE_CHECKING:
    import aws_sdk_ec2.types.create_vpc_endpoint_service_configuration_request
    import aws_sdk_ec2.types.create_vpc_endpoint_service_configuration_result


def create_vpc_endpoint_service_configuration(
    options: OperationOptions,
    input: aws_sdk_ec2.types.create_vpc_endpoint_service_configuration_request.CreateVpcEndpointServiceConfigurationRequest,
) -> tuple[
    aws_sdk_ec2.types.create_vpc_endpoint_service_configuration_result.CreateVpcEndpointServiceConfigurationResult,
    zapros.Response,
]:
    raise NotImplementedError("operation dispatch not yet generated")


async def async_create_vpc_endpoint_service_configuration(
    options: AsyncOperationOptions,
    input: aws_sdk_ec2.types.create_vpc_endpoint_service_configuration_request.CreateVpcEndpointServiceConfigurationRequest,
) -> tuple[
    aws_sdk_ec2.types.create_vpc_endpoint_service_configuration_result.CreateVpcEndpointServiceConfigurationResult,
    zapros.Response,
]:
    raise NotImplementedError("operation dispatch not yet generated")
