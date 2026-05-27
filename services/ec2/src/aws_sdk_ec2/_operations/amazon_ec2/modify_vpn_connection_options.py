"""Generated from Smithy shape ``com.amazonaws.ec2#ModifyVpnConnectionOptions``."""

from __future__ import annotations
from typing import TYPE_CHECKING
import zapros
import aws_sdk_ec2._auth._signers
from aws_sdk_ec2._services._pipeline import AsyncOperationOptions, OperationOptions

if TYPE_CHECKING:
    import aws_sdk_ec2.types.modify_vpn_connection_options_request
    import aws_sdk_ec2.types.modify_vpn_connection_options_result


def modify_vpn_connection_options(
    options: OperationOptions,
    input: aws_sdk_ec2.types.modify_vpn_connection_options_request.ModifyVpnConnectionOptionsRequest,
) -> tuple[
    aws_sdk_ec2.types.modify_vpn_connection_options_result.ModifyVpnConnectionOptionsResult,
    zapros.Response,
]:
    raise NotImplementedError("operation dispatch not yet generated")


async def async_modify_vpn_connection_options(
    options: AsyncOperationOptions,
    input: aws_sdk_ec2.types.modify_vpn_connection_options_request.ModifyVpnConnectionOptionsRequest,
) -> tuple[
    aws_sdk_ec2.types.modify_vpn_connection_options_result.ModifyVpnConnectionOptionsResult,
    zapros.Response,
]:
    raise NotImplementedError("operation dispatch not yet generated")
