"""Generated from Smithy shape ``com.amazonaws.ec2#DeprovisionByoipCidr``."""

from __future__ import annotations
from typing import TYPE_CHECKING
import zapros
import aws_sdk_ec2._auth._signers
from aws_sdk_ec2._services._pipeline import AsyncOperationOptions, OperationOptions

if TYPE_CHECKING:
    import aws_sdk_ec2.types.deprovision_byoip_cidr_request
    import aws_sdk_ec2.types.deprovision_byoip_cidr_result


def deprovision_byoip_cidr(
    options: OperationOptions,
    input: aws_sdk_ec2.types.deprovision_byoip_cidr_request.DeprovisionByoipCidrRequest,
) -> tuple[
    aws_sdk_ec2.types.deprovision_byoip_cidr_result.DeprovisionByoipCidrResult,
    zapros.Response,
]:
    raise NotImplementedError("operation dispatch not yet generated")


async def async_deprovision_byoip_cidr(
    options: AsyncOperationOptions,
    input: aws_sdk_ec2.types.deprovision_byoip_cidr_request.DeprovisionByoipCidrRequest,
) -> tuple[
    aws_sdk_ec2.types.deprovision_byoip_cidr_result.DeprovisionByoipCidrResult,
    zapros.Response,
]:
    raise NotImplementedError("operation dispatch not yet generated")
