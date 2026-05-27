"""Generated from Smithy shape ``com.amazonaws.ec2#RequestSpotFleet``."""

from __future__ import annotations
from typing import TYPE_CHECKING
import zapros
import aws_sdk_ec2._auth._signers
from aws_sdk_ec2._services._pipeline import AsyncOperationOptions, OperationOptions

if TYPE_CHECKING:
    import aws_sdk_ec2.types.request_spot_fleet_request
    import aws_sdk_ec2.types.request_spot_fleet_response


def request_spot_fleet(
    options: OperationOptions,
    input: aws_sdk_ec2.types.request_spot_fleet_request.RequestSpotFleetRequest,
) -> tuple[
    aws_sdk_ec2.types.request_spot_fleet_response.RequestSpotFleetResponse,
    zapros.Response,
]:
    raise NotImplementedError("operation dispatch not yet generated")


async def async_request_spot_fleet(
    options: AsyncOperationOptions,
    input: aws_sdk_ec2.types.request_spot_fleet_request.RequestSpotFleetRequest,
) -> tuple[
    aws_sdk_ec2.types.request_spot_fleet_response.RequestSpotFleetResponse,
    zapros.Response,
]:
    raise NotImplementedError("operation dispatch not yet generated")
