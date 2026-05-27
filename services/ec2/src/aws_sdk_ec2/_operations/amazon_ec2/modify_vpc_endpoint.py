"""Generated from Smithy shape ``com.amazonaws.ec2#ModifyVpcEndpoint``."""

from __future__ import annotations
from typing import TYPE_CHECKING
import zapros
import aws_sdk_ec2._auth._signers
from aws_sdk_ec2._services._pipeline import AsyncOperationOptions, OperationOptions

if TYPE_CHECKING:
    import aws_sdk_ec2.types.modify_vpc_endpoint_request
    import aws_sdk_ec2.types.modify_vpc_endpoint_result


def modify_vpc_endpoint(
    options: OperationOptions,
    input: aws_sdk_ec2.types.modify_vpc_endpoint_request.ModifyVpcEndpointRequest,
) -> tuple[
    aws_sdk_ec2.types.modify_vpc_endpoint_result.ModifyVpcEndpointResult,
    zapros.Response,
]:
    raise NotImplementedError("operation dispatch not yet generated")


async def async_modify_vpc_endpoint(
    options: AsyncOperationOptions,
    input: aws_sdk_ec2.types.modify_vpc_endpoint_request.ModifyVpcEndpointRequest,
) -> tuple[
    aws_sdk_ec2.types.modify_vpc_endpoint_result.ModifyVpcEndpointResult,
    zapros.Response,
]:
    raise NotImplementedError("operation dispatch not yet generated")
