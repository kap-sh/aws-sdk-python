"""Generated from Smithy shape ``com.amazonaws.ec2#ModifyVpcEndpointServicePayerResponsibility``."""

from __future__ import annotations
from typing import TYPE_CHECKING
import zapros
import aws_sdk_ec2._auth._signers
from aws_sdk_ec2._services._pipeline import AsyncOperationOptions, OperationOptions

if TYPE_CHECKING:
    import aws_sdk_ec2.types.modify_vpc_endpoint_service_payer_responsibility_request
    import aws_sdk_ec2.types.modify_vpc_endpoint_service_payer_responsibility_result


def modify_vpc_endpoint_service_payer_responsibility(
    options: OperationOptions,
    input: aws_sdk_ec2.types.modify_vpc_endpoint_service_payer_responsibility_request.ModifyVpcEndpointServicePayerResponsibilityRequest,
) -> tuple[
    aws_sdk_ec2.types.modify_vpc_endpoint_service_payer_responsibility_result.ModifyVpcEndpointServicePayerResponsibilityResult,
    zapros.Response,
]:
    raise NotImplementedError("operation dispatch not yet generated")


async def async_modify_vpc_endpoint_service_payer_responsibility(
    options: AsyncOperationOptions,
    input: aws_sdk_ec2.types.modify_vpc_endpoint_service_payer_responsibility_request.ModifyVpcEndpointServicePayerResponsibilityRequest,
) -> tuple[
    aws_sdk_ec2.types.modify_vpc_endpoint_service_payer_responsibility_result.ModifyVpcEndpointServicePayerResponsibilityResult,
    zapros.Response,
]:
    raise NotImplementedError("operation dispatch not yet generated")
