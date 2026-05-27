"""Generated from Smithy shape ``com.amazonaws.ec2#AdvertiseByoipCidr``."""

from __future__ import annotations
from typing import TYPE_CHECKING
import zapros
import aws_sdk_ec2._auth._signers
from aws_sdk_ec2._services._pipeline import AsyncOperationOptions, OperationOptions

if TYPE_CHECKING:
    import aws_sdk_ec2.types.advertise_byoip_cidr_request
    import aws_sdk_ec2.types.advertise_byoip_cidr_result


def advertise_byoip_cidr(
    options: OperationOptions,
    input: aws_sdk_ec2.types.advertise_byoip_cidr_request.AdvertiseByoipCidrRequest,
) -> tuple[
    aws_sdk_ec2.types.advertise_byoip_cidr_result.AdvertiseByoipCidrResult,
    zapros.Response,
]:
    raise NotImplementedError("operation dispatch not yet generated")


async def async_advertise_byoip_cidr(
    options: AsyncOperationOptions,
    input: aws_sdk_ec2.types.advertise_byoip_cidr_request.AdvertiseByoipCidrRequest,
) -> tuple[
    aws_sdk_ec2.types.advertise_byoip_cidr_result.AdvertiseByoipCidrResult,
    zapros.Response,
]:
    raise NotImplementedError("operation dispatch not yet generated")
