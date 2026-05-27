"""Generated from Smithy shape ``com.amazonaws.ec2#ExportClientVpnClientConfiguration``."""

from __future__ import annotations
from typing import TYPE_CHECKING
import zapros
import aws_sdk_ec2._auth._signers
from aws_sdk_ec2._services._pipeline import AsyncOperationOptions, OperationOptions

if TYPE_CHECKING:
    import aws_sdk_ec2.types.export_client_vpn_client_configuration_request
    import aws_sdk_ec2.types.export_client_vpn_client_configuration_result


def export_client_vpn_client_configuration(
    options: OperationOptions,
    input: aws_sdk_ec2.types.export_client_vpn_client_configuration_request.ExportClientVpnClientConfigurationRequest,
) -> tuple[
    aws_sdk_ec2.types.export_client_vpn_client_configuration_result.ExportClientVpnClientConfigurationResult,
    zapros.Response,
]:
    raise NotImplementedError("operation dispatch not yet generated")


async def async_export_client_vpn_client_configuration(
    options: AsyncOperationOptions,
    input: aws_sdk_ec2.types.export_client_vpn_client_configuration_request.ExportClientVpnClientConfigurationRequest,
) -> tuple[
    aws_sdk_ec2.types.export_client_vpn_client_configuration_result.ExportClientVpnClientConfigurationResult,
    zapros.Response,
]:
    raise NotImplementedError("operation dispatch not yet generated")
