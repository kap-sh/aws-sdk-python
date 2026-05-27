"""Generated from Smithy shape ``com.amazonaws.ec2#RunInstances``."""

from __future__ import annotations
from typing import TYPE_CHECKING
import zapros
import aws_sdk_ec2._auth._signers
from aws_sdk_ec2._services._pipeline import AsyncOperationOptions, OperationOptions

if TYPE_CHECKING:
    import aws_sdk_ec2.types.run_instances_request
    import aws_sdk_ec2.types.reservation


def run_instances(
    options: OperationOptions,
    input: aws_sdk_ec2.types.run_instances_request.RunInstancesRequest,
) -> tuple[aws_sdk_ec2.types.reservation.Reservation, zapros.Response]:
    raise NotImplementedError("operation dispatch not yet generated")


async def async_run_instances(
    options: AsyncOperationOptions,
    input: aws_sdk_ec2.types.run_instances_request.RunInstancesRequest,
) -> tuple[aws_sdk_ec2.types.reservation.Reservation, zapros.Response]:
    raise NotImplementedError("operation dispatch not yet generated")
