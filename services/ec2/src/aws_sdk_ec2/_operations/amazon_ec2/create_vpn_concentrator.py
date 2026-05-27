"""Generated from Smithy shape ``com.amazonaws.ec2#CreateVpnConcentrator``."""

from __future__ import annotations
from typing import TYPE_CHECKING
import zapros
import aws_sdk_ec2._auth._signers
from aws_sdk_ec2._services._pipeline import AsyncOperationOptions, OperationOptions

if TYPE_CHECKING:
    import aws_sdk_ec2.types.create_vpn_concentrator_request
    import aws_sdk_ec2.types.create_vpn_concentrator_result


def create_vpn_concentrator(
    options: OperationOptions,
    input: aws_sdk_ec2.types.create_vpn_concentrator_request.CreateVpnConcentratorRequest,
) -> tuple[
    aws_sdk_ec2.types.create_vpn_concentrator_result.CreateVpnConcentratorResult,
    zapros.Response,
]:
    raise NotImplementedError("operation dispatch not yet generated")


async def async_create_vpn_concentrator(
    options: AsyncOperationOptions,
    input: aws_sdk_ec2.types.create_vpn_concentrator_request.CreateVpnConcentratorRequest,
) -> tuple[
    aws_sdk_ec2.types.create_vpn_concentrator_result.CreateVpnConcentratorResult,
    zapros.Response,
]:
    raise NotImplementedError("operation dispatch not yet generated")
