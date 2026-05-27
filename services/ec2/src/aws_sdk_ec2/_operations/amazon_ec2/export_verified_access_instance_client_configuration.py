"""Generated from Smithy shape ``com.amazonaws.ec2#ExportVerifiedAccessInstanceClientConfiguration``."""

from __future__ import annotations
from typing import TYPE_CHECKING
import zapros
import aws_sdk_ec2._auth._signers
from aws_sdk_ec2._services._pipeline import AsyncOperationOptions, OperationOptions

if TYPE_CHECKING:
    import aws_sdk_ec2.types.export_verified_access_instance_client_configuration_request
    import aws_sdk_ec2.types.export_verified_access_instance_client_configuration_result


def export_verified_access_instance_client_configuration(
    options: OperationOptions,
    input: aws_sdk_ec2.types.export_verified_access_instance_client_configuration_request.ExportVerifiedAccessInstanceClientConfigurationRequest,
) -> tuple[
    aws_sdk_ec2.types.export_verified_access_instance_client_configuration_result.ExportVerifiedAccessInstanceClientConfigurationResult,
    zapros.Response,
]:
    raise NotImplementedError("operation dispatch not yet generated")


async def async_export_verified_access_instance_client_configuration(
    options: AsyncOperationOptions,
    input: aws_sdk_ec2.types.export_verified_access_instance_client_configuration_request.ExportVerifiedAccessInstanceClientConfigurationRequest,
) -> tuple[
    aws_sdk_ec2.types.export_verified_access_instance_client_configuration_result.ExportVerifiedAccessInstanceClientConfigurationResult,
    zapros.Response,
]:
    raise NotImplementedError("operation dispatch not yet generated")
