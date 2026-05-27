"""Generated from Smithy shape ``com.amazonaws.ec2#MoveCapacityReservationInstances``."""

from __future__ import annotations
from typing import TYPE_CHECKING
import zapros
import aws_sdk_ec2._auth._signers
from aws_sdk_ec2._services._pipeline import AsyncOperationOptions, OperationOptions

if TYPE_CHECKING:
    import aws_sdk_ec2.types.move_capacity_reservation_instances_request
    import aws_sdk_ec2.types.move_capacity_reservation_instances_result


def move_capacity_reservation_instances(
    options: OperationOptions,
    input: aws_sdk_ec2.types.move_capacity_reservation_instances_request.MoveCapacityReservationInstancesRequest,
) -> tuple[
    aws_sdk_ec2.types.move_capacity_reservation_instances_result.MoveCapacityReservationInstancesResult,
    zapros.Response,
]:
    raise NotImplementedError("operation dispatch not yet generated")


async def async_move_capacity_reservation_instances(
    options: AsyncOperationOptions,
    input: aws_sdk_ec2.types.move_capacity_reservation_instances_request.MoveCapacityReservationInstancesRequest,
) -> tuple[
    aws_sdk_ec2.types.move_capacity_reservation_instances_result.MoveCapacityReservationInstancesResult,
    zapros.Response,
]:
    raise NotImplementedError("operation dispatch not yet generated")
