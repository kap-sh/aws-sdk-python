"""Generated from Smithy shape ``com.amazonaws.ec2#StartVpcEndpointServicePrivateDnsVerification``."""

from __future__ import annotations
from typing import TYPE_CHECKING
import zapros
import aws_sdk_ec2._auth._signers
from aws_sdk_ec2._services._pipeline import AsyncOperationOptions, OperationOptions

if TYPE_CHECKING:
    import aws_sdk_ec2.types.start_vpc_endpoint_service_private_dns_verification_request
    import aws_sdk_ec2.types.start_vpc_endpoint_service_private_dns_verification_result


def start_vpc_endpoint_service_private_dns_verification(
    options: OperationOptions,
    input: aws_sdk_ec2.types.start_vpc_endpoint_service_private_dns_verification_request.StartVpcEndpointServicePrivateDnsVerificationRequest,
) -> tuple[
    aws_sdk_ec2.types.start_vpc_endpoint_service_private_dns_verification_result.StartVpcEndpointServicePrivateDnsVerificationResult,
    zapros.Response,
]:
    raise NotImplementedError("operation dispatch not yet generated")


async def async_start_vpc_endpoint_service_private_dns_verification(
    options: AsyncOperationOptions,
    input: aws_sdk_ec2.types.start_vpc_endpoint_service_private_dns_verification_request.StartVpcEndpointServicePrivateDnsVerificationRequest,
) -> tuple[
    aws_sdk_ec2.types.start_vpc_endpoint_service_private_dns_verification_result.StartVpcEndpointServicePrivateDnsVerificationResult,
    zapros.Response,
]:
    raise NotImplementedError("operation dispatch not yet generated")
