"""Generated from Smithy shape ``com.amazonaws.ec2#CreateCapacityReservationFleet``."""

from __future__ import annotations
from typing import TYPE_CHECKING
import zapros
import aws_sdk_ec2._auth._signers
from aws_sdk_ec2._services._pipeline import AsyncOperationOptions, OperationOptions

if TYPE_CHECKING:
    import aws_sdk_ec2.types.create_capacity_reservation_fleet_request
    import aws_sdk_ec2.types.create_capacity_reservation_fleet_result


def create_capacity_reservation_fleet(
    options: OperationOptions,
    input: aws_sdk_ec2.types.create_capacity_reservation_fleet_request.CreateCapacityReservationFleetRequest,
) -> tuple[
    aws_sdk_ec2.types.create_capacity_reservation_fleet_result.CreateCapacityReservationFleetResult,
    zapros.Response,
]:
    raise NotImplementedError("operation dispatch not yet generated")


async def async_create_capacity_reservation_fleet(
    options: AsyncOperationOptions,
    input: aws_sdk_ec2.types.create_capacity_reservation_fleet_request.CreateCapacityReservationFleetRequest,
) -> tuple[
    aws_sdk_ec2.types.create_capacity_reservation_fleet_result.CreateCapacityReservationFleetResult,
    zapros.Response,
]:
    raise NotImplementedError("operation dispatch not yet generated")
