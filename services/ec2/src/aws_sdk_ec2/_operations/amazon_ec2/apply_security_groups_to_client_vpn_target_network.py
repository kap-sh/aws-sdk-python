"""Generated from Smithy shape ``com.amazonaws.ec2#ApplySecurityGroupsToClientVpnTargetNetwork``."""

from __future__ import annotations
from typing import TYPE_CHECKING
import zapros
import aws_sdk_ec2._auth._signers
from aws_sdk_ec2._services._pipeline import AsyncOperationOptions, OperationOptions

if TYPE_CHECKING:
    import aws_sdk_ec2.types.apply_security_groups_to_client_vpn_target_network_request
    import aws_sdk_ec2.types.apply_security_groups_to_client_vpn_target_network_result


def apply_security_groups_to_client_vpn_target_network(
    options: OperationOptions,
    input: aws_sdk_ec2.types.apply_security_groups_to_client_vpn_target_network_request.ApplySecurityGroupsToClientVpnTargetNetworkRequest,
) -> tuple[
    aws_sdk_ec2.types.apply_security_groups_to_client_vpn_target_network_result.ApplySecurityGroupsToClientVpnTargetNetworkResult,
    zapros.Response,
]:
    raise NotImplementedError("operation dispatch not yet generated")


async def async_apply_security_groups_to_client_vpn_target_network(
    options: AsyncOperationOptions,
    input: aws_sdk_ec2.types.apply_security_groups_to_client_vpn_target_network_request.ApplySecurityGroupsToClientVpnTargetNetworkRequest,
) -> tuple[
    aws_sdk_ec2.types.apply_security_groups_to_client_vpn_target_network_result.ApplySecurityGroupsToClientVpnTargetNetworkResult,
    zapros.Response,
]:
    raise NotImplementedError("operation dispatch not yet generated")
