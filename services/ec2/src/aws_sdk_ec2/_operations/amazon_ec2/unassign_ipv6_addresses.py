"""Generated from Smithy shape ``com.amazonaws.ec2#UnassignIpv6Addresses``."""

from __future__ import annotations
from typing import TYPE_CHECKING
import zapros
import aws_sdk_ec2._auth._signers
from aws_sdk_ec2._services._pipeline import AsyncOperationOptions, OperationOptions

if TYPE_CHECKING:
    import aws_sdk_ec2.types.unassign_ipv6_addresses_request
    import aws_sdk_ec2.types.unassign_ipv6_addresses_result


def unassign_ipv6_addresses(
    options: OperationOptions,
    input: aws_sdk_ec2.types.unassign_ipv6_addresses_request.UnassignIpv6AddressesRequest,
) -> tuple[
    aws_sdk_ec2.types.unassign_ipv6_addresses_result.UnassignIpv6AddressesResult,
    zapros.Response,
]:
    raise NotImplementedError("operation dispatch not yet generated")


async def async_unassign_ipv6_addresses(
    options: AsyncOperationOptions,
    input: aws_sdk_ec2.types.unassign_ipv6_addresses_request.UnassignIpv6AddressesRequest,
) -> tuple[
    aws_sdk_ec2.types.unassign_ipv6_addresses_result.UnassignIpv6AddressesResult,
    zapros.Response,
]:
    raise NotImplementedError("operation dispatch not yet generated")
