"""Generated from Smithy shape ``com.amazonaws.ec2#GetIpamDiscoveredAccounts``."""

from __future__ import annotations
from typing import TYPE_CHECKING
import zapros
import aws_sdk_ec2._auth._signers
from aws_sdk_ec2._services._pipeline import AsyncOperationOptions, OperationOptions

if TYPE_CHECKING:
    import aws_sdk_ec2.types.get_ipam_discovered_accounts_request
    import aws_sdk_ec2.types.get_ipam_discovered_accounts_result


def get_ipam_discovered_accounts(
    options: OperationOptions,
    input: aws_sdk_ec2.types.get_ipam_discovered_accounts_request.GetIpamDiscoveredAccountsRequest,
) -> tuple[
    aws_sdk_ec2.types.get_ipam_discovered_accounts_result.GetIpamDiscoveredAccountsResult,
    zapros.Response,
]:
    raise NotImplementedError("operation dispatch not yet generated")


async def async_get_ipam_discovered_accounts(
    options: AsyncOperationOptions,
    input: aws_sdk_ec2.types.get_ipam_discovered_accounts_request.GetIpamDiscoveredAccountsRequest,
) -> tuple[
    aws_sdk_ec2.types.get_ipam_discovered_accounts_result.GetIpamDiscoveredAccountsResult,
    zapros.Response,
]:
    raise NotImplementedError("operation dispatch not yet generated")
