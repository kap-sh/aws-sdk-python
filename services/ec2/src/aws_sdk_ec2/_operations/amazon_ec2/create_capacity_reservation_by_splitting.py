"""Generated from Smithy shape ``com.amazonaws.ec2#CreateCapacityReservationBySplitting``."""

from __future__ import annotations
from typing import TYPE_CHECKING
import zapros
import aws_sdk_ec2._auth._signers
from aws_sdk_ec2._services._pipeline import AsyncOperationOptions, OperationOptions

if TYPE_CHECKING:
    import aws_sdk_ec2.types.create_capacity_reservation_by_splitting_request
    import aws_sdk_ec2.types.create_capacity_reservation_by_splitting_result


def create_capacity_reservation_by_splitting(
    options: OperationOptions,
    input: aws_sdk_ec2.types.create_capacity_reservation_by_splitting_request.CreateCapacityReservationBySplittingRequest,
) -> tuple[
    aws_sdk_ec2.types.create_capacity_reservation_by_splitting_result.CreateCapacityReservationBySplittingResult,
    zapros.Response,
]:
    raise NotImplementedError("operation dispatch not yet generated")


async def async_create_capacity_reservation_by_splitting(
    options: AsyncOperationOptions,
    input: aws_sdk_ec2.types.create_capacity_reservation_by_splitting_request.CreateCapacityReservationBySplittingRequest,
) -> tuple[
    aws_sdk_ec2.types.create_capacity_reservation_by_splitting_result.CreateCapacityReservationBySplittingResult,
    zapros.Response,
]:
    raise NotImplementedError("operation dispatch not yet generated")
