"""Generated from Smithy shape ``com.amazonaws.ec2#DisassociateClientVpnTargetNetwork``."""

from __future__ import annotations
from typing import TYPE_CHECKING
import zapros
import aws_sdk_ec2._auth._signers
from aws_sdk_ec2._services._pipeline import AsyncOperationOptions, OperationOptions

if TYPE_CHECKING:
    import aws_sdk_ec2.types.disassociate_client_vpn_target_network_request
    import aws_sdk_ec2.types.disassociate_client_vpn_target_network_result


def disassociate_client_vpn_target_network(
    options: OperationOptions,
    input: aws_sdk_ec2.types.disassociate_client_vpn_target_network_request.DisassociateClientVpnTargetNetworkRequest,
) -> tuple[
    aws_sdk_ec2.types.disassociate_client_vpn_target_network_result.DisassociateClientVpnTargetNetworkResult,
    zapros.Response,
]:
    raise NotImplementedError("operation dispatch not yet generated")


async def async_disassociate_client_vpn_target_network(
    options: AsyncOperationOptions,
    input: aws_sdk_ec2.types.disassociate_client_vpn_target_network_request.DisassociateClientVpnTargetNetworkRequest,
) -> tuple[
    aws_sdk_ec2.types.disassociate_client_vpn_target_network_result.DisassociateClientVpnTargetNetworkResult,
    zapros.Response,
]:
    raise NotImplementedError("operation dispatch not yet generated")
