"""Generated from Smithy shape ``com.amazonaws.ec2#CancelSpotInstanceRequests``."""

from __future__ import annotations
from typing import TYPE_CHECKING
import zapros
import aws_sdk_ec2._auth._signers
from aws_sdk_ec2._services._pipeline import AsyncOperationOptions, OperationOptions

if TYPE_CHECKING:
    import aws_sdk_ec2.types.cancel_spot_instance_requests_request
    import aws_sdk_ec2.types.cancel_spot_instance_requests_result


def cancel_spot_instance_requests(
    options: OperationOptions,
    input: aws_sdk_ec2.types.cancel_spot_instance_requests_request.CancelSpotInstanceRequestsRequest,
) -> tuple[
    aws_sdk_ec2.types.cancel_spot_instance_requests_result.CancelSpotInstanceRequestsResult,
    zapros.Response,
]:
    raise NotImplementedError("operation dispatch not yet generated")


async def async_cancel_spot_instance_requests(
    options: AsyncOperationOptions,
    input: aws_sdk_ec2.types.cancel_spot_instance_requests_request.CancelSpotInstanceRequestsRequest,
) -> tuple[
    aws_sdk_ec2.types.cancel_spot_instance_requests_result.CancelSpotInstanceRequestsResult,
    zapros.Response,
]:
    raise NotImplementedError("operation dispatch not yet generated")
