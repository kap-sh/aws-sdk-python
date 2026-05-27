"""Generated from Smithy shape ``com.amazonaws.ec2#AssignPrivateIpAddresses``."""

from __future__ import annotations
from typing import TYPE_CHECKING
import zapros
import aws_sdk_ec2._auth._signers
from aws_sdk_ec2._services._pipeline import AsyncOperationOptions, OperationOptions

if TYPE_CHECKING:
    import aws_sdk_ec2.types.assign_private_ip_addresses_request
    import aws_sdk_ec2.types.assign_private_ip_addresses_result


def assign_private_ip_addresses(
    options: OperationOptions,
    input: aws_sdk_ec2.types.assign_private_ip_addresses_request.AssignPrivateIpAddressesRequest,
) -> tuple[
    aws_sdk_ec2.types.assign_private_ip_addresses_result.AssignPrivateIpAddressesResult,
    zapros.Response,
]:
    raise NotImplementedError("operation dispatch not yet generated")


async def async_assign_private_ip_addresses(
    options: AsyncOperationOptions,
    input: aws_sdk_ec2.types.assign_private_ip_addresses_request.AssignPrivateIpAddressesRequest,
) -> tuple[
    aws_sdk_ec2.types.assign_private_ip_addresses_result.AssignPrivateIpAddressesResult,
    zapros.Response,
]:
    raise NotImplementedError("operation dispatch not yet generated")
