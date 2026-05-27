"""Generated from Smithy shape ``com.amazonaws.ec2#GetGroupsForCapacityReservation``."""

from __future__ import annotations
from typing import TYPE_CHECKING
import zapros
import aws_sdk_ec2._auth._signers
from aws_sdk_ec2._services._pipeline import AsyncOperationOptions, OperationOptions

if TYPE_CHECKING:
    import aws_sdk_ec2.types.get_groups_for_capacity_reservation_request
    import aws_sdk_ec2.types.get_groups_for_capacity_reservation_result


def get_groups_for_capacity_reservation(
    options: OperationOptions,
    input: aws_sdk_ec2.types.get_groups_for_capacity_reservation_request.GetGroupsForCapacityReservationRequest,
) -> tuple[
    aws_sdk_ec2.types.get_groups_for_capacity_reservation_result.GetGroupsForCapacityReservationResult,
    zapros.Response,
]:
    raise NotImplementedError("operation dispatch not yet generated")


async def async_get_groups_for_capacity_reservation(
    options: AsyncOperationOptions,
    input: aws_sdk_ec2.types.get_groups_for_capacity_reservation_request.GetGroupsForCapacityReservationRequest,
) -> tuple[
    aws_sdk_ec2.types.get_groups_for_capacity_reservation_result.GetGroupsForCapacityReservationResult,
    zapros.Response,
]:
    raise NotImplementedError("operation dispatch not yet generated")
