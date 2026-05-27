"""Generated from Smithy shape ``com.amazonaws.ec2#CreateInterruptibleCapacityReservationAllocation``."""

from __future__ import annotations
from typing import TYPE_CHECKING
import zapros
import aws_sdk_ec2._auth._signers
from aws_sdk_ec2._services._pipeline import AsyncOperationOptions, OperationOptions

if TYPE_CHECKING:
    import aws_sdk_ec2.types.create_interruptible_capacity_reservation_allocation_request
    import aws_sdk_ec2.types.create_interruptible_capacity_reservation_allocation_result


def create_interruptible_capacity_reservation_allocation(
    options: OperationOptions,
    input: aws_sdk_ec2.types.create_interruptible_capacity_reservation_allocation_request.CreateInterruptibleCapacityReservationAllocationRequest,
) -> tuple[
    aws_sdk_ec2.types.create_interruptible_capacity_reservation_allocation_result.CreateInterruptibleCapacityReservationAllocationResult,
    zapros.Response,
]:
    raise NotImplementedError("operation dispatch not yet generated")


async def async_create_interruptible_capacity_reservation_allocation(
    options: AsyncOperationOptions,
    input: aws_sdk_ec2.types.create_interruptible_capacity_reservation_allocation_request.CreateInterruptibleCapacityReservationAllocationRequest,
) -> tuple[
    aws_sdk_ec2.types.create_interruptible_capacity_reservation_allocation_result.CreateInterruptibleCapacityReservationAllocationResult,
    zapros.Response,
]:
    raise NotImplementedError("operation dispatch not yet generated")
