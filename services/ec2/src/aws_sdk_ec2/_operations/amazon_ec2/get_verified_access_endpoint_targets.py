"""Generated from Smithy shape ``com.amazonaws.ec2#GetVerifiedAccessEndpointTargets``."""

from __future__ import annotations
from typing import TYPE_CHECKING
import zapros
import aws_sdk_ec2._auth._signers
from aws_sdk_ec2._services._pipeline import AsyncOperationOptions, OperationOptions

if TYPE_CHECKING:
    import aws_sdk_ec2.types.get_verified_access_endpoint_targets_request
    import aws_sdk_ec2.types.get_verified_access_endpoint_targets_result


def get_verified_access_endpoint_targets(
    options: OperationOptions,
    input: aws_sdk_ec2.types.get_verified_access_endpoint_targets_request.GetVerifiedAccessEndpointTargetsRequest,
) -> tuple[
    aws_sdk_ec2.types.get_verified_access_endpoint_targets_result.GetVerifiedAccessEndpointTargetsResult,
    zapros.Response,
]:
    raise NotImplementedError("operation dispatch not yet generated")


async def async_get_verified_access_endpoint_targets(
    options: AsyncOperationOptions,
    input: aws_sdk_ec2.types.get_verified_access_endpoint_targets_request.GetVerifiedAccessEndpointTargetsRequest,
) -> tuple[
    aws_sdk_ec2.types.get_verified_access_endpoint_targets_result.GetVerifiedAccessEndpointTargetsResult,
    zapros.Response,
]:
    raise NotImplementedError("operation dispatch not yet generated")
