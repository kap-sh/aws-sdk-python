"""Generated from Smithy shape ``com.amazonaws.ec2#UnassignPrivateIpAddresses``."""

from __future__ import annotations
from typing import TYPE_CHECKING
import zapros
import aws_sdk_ec2._auth._signers
from aws_sdk_ec2._services._pipeline import AsyncOperationOptions, OperationOptions

if TYPE_CHECKING:
    import aws_sdk_ec2.types.unassign_private_ip_addresses_request


def unassign_private_ip_addresses(
    options: OperationOptions,
    input: aws_sdk_ec2.types.unassign_private_ip_addresses_request.UnassignPrivateIpAddressesRequest,
) -> tuple[None, zapros.Response]:
    raise NotImplementedError("operation dispatch not yet generated")


async def async_unassign_private_ip_addresses(
    options: AsyncOperationOptions,
    input: aws_sdk_ec2.types.unassign_private_ip_addresses_request.UnassignPrivateIpAddressesRequest,
) -> tuple[None, zapros.Response]:
    raise NotImplementedError("operation dispatch not yet generated")
