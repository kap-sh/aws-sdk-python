"""Generated from Smithy shape ``com.amazonaws.ec2#MoveByoipCidrToIpam``."""

from __future__ import annotations
from typing import TYPE_CHECKING
import zapros
import aws_sdk_ec2._auth._signers
from aws_sdk_ec2._services._pipeline import AsyncOperationOptions, OperationOptions

if TYPE_CHECKING:
    import aws_sdk_ec2.types.move_byoip_cidr_to_ipam_request
    import aws_sdk_ec2.types.move_byoip_cidr_to_ipam_result


def move_byoip_cidr_to_ipam(
    options: OperationOptions,
    input: aws_sdk_ec2.types.move_byoip_cidr_to_ipam_request.MoveByoipCidrToIpamRequest,
) -> tuple[
    aws_sdk_ec2.types.move_byoip_cidr_to_ipam_result.MoveByoipCidrToIpamResult,
    zapros.Response,
]:
    raise NotImplementedError("operation dispatch not yet generated")


async def async_move_byoip_cidr_to_ipam(
    options: AsyncOperationOptions,
    input: aws_sdk_ec2.types.move_byoip_cidr_to_ipam_request.MoveByoipCidrToIpamRequest,
) -> tuple[
    aws_sdk_ec2.types.move_byoip_cidr_to_ipam_result.MoveByoipCidrToIpamResult,
    zapros.Response,
]:
    raise NotImplementedError("operation dispatch not yet generated")
