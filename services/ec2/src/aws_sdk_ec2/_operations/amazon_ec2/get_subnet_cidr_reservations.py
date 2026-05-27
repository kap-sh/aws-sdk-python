"""Generated from Smithy shape ``com.amazonaws.ec2#GetSubnetCidrReservations``."""

from __future__ import annotations
from typing import TYPE_CHECKING
import zapros
import aws_sdk_ec2._auth._signers
from aws_sdk_ec2._services._pipeline import AsyncOperationOptions, OperationOptions

if TYPE_CHECKING:
    import aws_sdk_ec2.types.get_subnet_cidr_reservations_request
    import aws_sdk_ec2.types.get_subnet_cidr_reservations_result


def get_subnet_cidr_reservations(
    options: OperationOptions,
    input: aws_sdk_ec2.types.get_subnet_cidr_reservations_request.GetSubnetCidrReservationsRequest,
) -> tuple[
    aws_sdk_ec2.types.get_subnet_cidr_reservations_result.GetSubnetCidrReservationsResult,
    zapros.Response,
]:
    raise NotImplementedError("operation dispatch not yet generated")


async def async_get_subnet_cidr_reservations(
    options: AsyncOperationOptions,
    input: aws_sdk_ec2.types.get_subnet_cidr_reservations_request.GetSubnetCidrReservationsRequest,
) -> tuple[
    aws_sdk_ec2.types.get_subnet_cidr_reservations_result.GetSubnetCidrReservationsResult,
    zapros.Response,
]:
    raise NotImplementedError("operation dispatch not yet generated")
