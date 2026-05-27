"""Generated from Smithy shape ``com.amazonaws.ec2#GetIpamDiscoveredPublicAddresses``."""

from __future__ import annotations
from typing import TYPE_CHECKING
import zapros
import aws_sdk_ec2._auth._signers
from aws_sdk_ec2._services._pipeline import AsyncOperationOptions, OperationOptions

if TYPE_CHECKING:
    import aws_sdk_ec2.types.get_ipam_discovered_public_addresses_request
    import aws_sdk_ec2.types.get_ipam_discovered_public_addresses_result


def get_ipam_discovered_public_addresses(
    options: OperationOptions,
    input: aws_sdk_ec2.types.get_ipam_discovered_public_addresses_request.GetIpamDiscoveredPublicAddressesRequest,
) -> tuple[
    aws_sdk_ec2.types.get_ipam_discovered_public_addresses_result.GetIpamDiscoveredPublicAddressesResult,
    zapros.Response,
]:
    raise NotImplementedError("operation dispatch not yet generated")


async def async_get_ipam_discovered_public_addresses(
    options: AsyncOperationOptions,
    input: aws_sdk_ec2.types.get_ipam_discovered_public_addresses_request.GetIpamDiscoveredPublicAddressesRequest,
) -> tuple[
    aws_sdk_ec2.types.get_ipam_discovered_public_addresses_result.GetIpamDiscoveredPublicAddressesResult,
    zapros.Response,
]:
    raise NotImplementedError("operation dispatch not yet generated")
