"""Generated from Smithy shape ``com.amazonaws.ec2#CreateIpamResourceDiscovery``."""

from __future__ import annotations
from typing import TYPE_CHECKING
import zapros
import aws_sdk_ec2._auth._signers
from aws_sdk_ec2._services._pipeline import AsyncOperationOptions, OperationOptions

if TYPE_CHECKING:
    import aws_sdk_ec2.types.create_ipam_resource_discovery_request
    import aws_sdk_ec2.types.create_ipam_resource_discovery_result


def create_ipam_resource_discovery(
    options: OperationOptions,
    input: aws_sdk_ec2.types.create_ipam_resource_discovery_request.CreateIpamResourceDiscoveryRequest,
) -> tuple[
    aws_sdk_ec2.types.create_ipam_resource_discovery_result.CreateIpamResourceDiscoveryResult,
    zapros.Response,
]:
    raise NotImplementedError("operation dispatch not yet generated")


async def async_create_ipam_resource_discovery(
    options: AsyncOperationOptions,
    input: aws_sdk_ec2.types.create_ipam_resource_discovery_request.CreateIpamResourceDiscoveryRequest,
) -> tuple[
    aws_sdk_ec2.types.create_ipam_resource_discovery_result.CreateIpamResourceDiscoveryResult,
    zapros.Response,
]:
    raise NotImplementedError("operation dispatch not yet generated")
