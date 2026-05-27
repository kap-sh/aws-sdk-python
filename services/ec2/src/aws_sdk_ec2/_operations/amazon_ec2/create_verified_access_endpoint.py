"""Generated from Smithy shape ``com.amazonaws.ec2#CreateVerifiedAccessEndpoint``."""

from __future__ import annotations
from typing import TYPE_CHECKING
import zapros
import aws_sdk_ec2._auth._signers
from aws_sdk_ec2._services._pipeline import AsyncOperationOptions, OperationOptions

if TYPE_CHECKING:
    import aws_sdk_ec2.types.create_verified_access_endpoint_request
    import aws_sdk_ec2.types.create_verified_access_endpoint_result


def create_verified_access_endpoint(
    options: OperationOptions,
    input: aws_sdk_ec2.types.create_verified_access_endpoint_request.CreateVerifiedAccessEndpointRequest,
) -> tuple[
    aws_sdk_ec2.types.create_verified_access_endpoint_result.CreateVerifiedAccessEndpointResult,
    zapros.Response,
]:
    raise NotImplementedError("operation dispatch not yet generated")


async def async_create_verified_access_endpoint(
    options: AsyncOperationOptions,
    input: aws_sdk_ec2.types.create_verified_access_endpoint_request.CreateVerifiedAccessEndpointRequest,
) -> tuple[
    aws_sdk_ec2.types.create_verified_access_endpoint_result.CreateVerifiedAccessEndpointResult,
    zapros.Response,
]:
    raise NotImplementedError("operation dispatch not yet generated")
