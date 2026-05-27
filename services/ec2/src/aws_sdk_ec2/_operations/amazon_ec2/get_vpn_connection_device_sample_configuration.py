"""Generated from Smithy shape ``com.amazonaws.ec2#GetVpnConnectionDeviceSampleConfiguration``."""

from __future__ import annotations
from typing import TYPE_CHECKING
import zapros
import aws_sdk_ec2._auth._signers
from aws_sdk_ec2._services._pipeline import AsyncOperationOptions, OperationOptions

if TYPE_CHECKING:
    import aws_sdk_ec2.types.get_vpn_connection_device_sample_configuration_request
    import aws_sdk_ec2.types.get_vpn_connection_device_sample_configuration_result


def get_vpn_connection_device_sample_configuration(
    options: OperationOptions,
    input: aws_sdk_ec2.types.get_vpn_connection_device_sample_configuration_request.GetVpnConnectionDeviceSampleConfigurationRequest,
) -> tuple[
    aws_sdk_ec2.types.get_vpn_connection_device_sample_configuration_result.GetVpnConnectionDeviceSampleConfigurationResult,
    zapros.Response,
]:
    raise NotImplementedError("operation dispatch not yet generated")


async def async_get_vpn_connection_device_sample_configuration(
    options: AsyncOperationOptions,
    input: aws_sdk_ec2.types.get_vpn_connection_device_sample_configuration_request.GetVpnConnectionDeviceSampleConfigurationRequest,
) -> tuple[
    aws_sdk_ec2.types.get_vpn_connection_device_sample_configuration_result.GetVpnConnectionDeviceSampleConfigurationResult,
    zapros.Response,
]:
    raise NotImplementedError("operation dispatch not yet generated")
