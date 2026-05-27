"""Generated from Smithy shape ``com.amazonaws.ec2#DeleteSubnetCidrReservation``."""

from __future__ import annotations
from typing import TYPE_CHECKING
import zapros
import aws_sdk_ec2._auth._signers
from aws_sdk_ec2._services._pipeline import AsyncOperationOptions, OperationOptions

if TYPE_CHECKING:
    import aws_sdk_ec2.types.delete_subnet_cidr_reservation_request
    import aws_sdk_ec2.types.delete_subnet_cidr_reservation_result


def delete_subnet_cidr_reservation(
    options: OperationOptions,
    input: aws_sdk_ec2.types.delete_subnet_cidr_reservation_request.DeleteSubnetCidrReservationRequest,
) -> tuple[
    aws_sdk_ec2.types.delete_subnet_cidr_reservation_result.DeleteSubnetCidrReservationResult,
    zapros.Response,
]:
    raise NotImplementedError("operation dispatch not yet generated")


async def async_delete_subnet_cidr_reservation(
    options: AsyncOperationOptions,
    input: aws_sdk_ec2.types.delete_subnet_cidr_reservation_request.DeleteSubnetCidrReservationRequest,
) -> tuple[
    aws_sdk_ec2.types.delete_subnet_cidr_reservation_result.DeleteSubnetCidrReservationResult,
    zapros.Response,
]:
    raise NotImplementedError("operation dispatch not yet generated")
