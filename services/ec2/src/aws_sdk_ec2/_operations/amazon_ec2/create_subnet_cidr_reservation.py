"""Generated from Smithy shape ``com.amazonaws.ec2#CreateSubnetCidrReservation``."""

from __future__ import annotations
from typing import TYPE_CHECKING
import zapros
import aws_sdk_ec2._auth._signers
from aws_sdk_ec2._services._pipeline import AsyncOperationOptions, OperationOptions

if TYPE_CHECKING:
    import aws_sdk_ec2.types.create_subnet_cidr_reservation_request
    import aws_sdk_ec2.types.create_subnet_cidr_reservation_result


def create_subnet_cidr_reservation(
    options: OperationOptions,
    input: aws_sdk_ec2.types.create_subnet_cidr_reservation_request.CreateSubnetCidrReservationRequest,
) -> tuple[
    aws_sdk_ec2.types.create_subnet_cidr_reservation_result.CreateSubnetCidrReservationResult,
    zapros.Response,
]:
    raise NotImplementedError("operation dispatch not yet generated")


async def async_create_subnet_cidr_reservation(
    options: AsyncOperationOptions,
    input: aws_sdk_ec2.types.create_subnet_cidr_reservation_request.CreateSubnetCidrReservationRequest,
) -> tuple[
    aws_sdk_ec2.types.create_subnet_cidr_reservation_result.CreateSubnetCidrReservationResult,
    zapros.Response,
]:
    raise NotImplementedError("operation dispatch not yet generated")
