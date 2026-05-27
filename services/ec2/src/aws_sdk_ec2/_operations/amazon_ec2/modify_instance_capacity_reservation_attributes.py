"""Generated from Smithy shape ``com.amazonaws.ec2#ModifyInstanceCapacityReservationAttributes``."""

from __future__ import annotations
from typing import TYPE_CHECKING
import zapros
import aws_sdk_ec2._auth._signers
from aws_sdk_ec2._services._pipeline import AsyncOperationOptions, OperationOptions

if TYPE_CHECKING:
    import aws_sdk_ec2.types.modify_instance_capacity_reservation_attributes_request
    import aws_sdk_ec2.types.modify_instance_capacity_reservation_attributes_result


def modify_instance_capacity_reservation_attributes(
    options: OperationOptions,
    input: aws_sdk_ec2.types.modify_instance_capacity_reservation_attributes_request.ModifyInstanceCapacityReservationAttributesRequest,
) -> tuple[
    aws_sdk_ec2.types.modify_instance_capacity_reservation_attributes_result.ModifyInstanceCapacityReservationAttributesResult,
    zapros.Response,
]:
    raise NotImplementedError("operation dispatch not yet generated")


async def async_modify_instance_capacity_reservation_attributes(
    options: AsyncOperationOptions,
    input: aws_sdk_ec2.types.modify_instance_capacity_reservation_attributes_request.ModifyInstanceCapacityReservationAttributesRequest,
) -> tuple[
    aws_sdk_ec2.types.modify_instance_capacity_reservation_attributes_result.ModifyInstanceCapacityReservationAttributesResult,
    zapros.Response,
]:
    raise NotImplementedError("operation dispatch not yet generated")
