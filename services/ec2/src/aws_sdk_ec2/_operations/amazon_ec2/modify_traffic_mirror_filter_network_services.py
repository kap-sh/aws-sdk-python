"""Generated from Smithy shape ``com.amazonaws.ec2#ModifyTrafficMirrorFilterNetworkServices``."""

from __future__ import annotations
from typing import TYPE_CHECKING
import zapros
import aws_sdk_ec2._auth._signers
from aws_sdk_ec2._services._pipeline import AsyncOperationOptions, OperationOptions

if TYPE_CHECKING:
    import aws_sdk_ec2.types.modify_traffic_mirror_filter_network_services_request
    import aws_sdk_ec2.types.modify_traffic_mirror_filter_network_services_result


def modify_traffic_mirror_filter_network_services(
    options: OperationOptions,
    input: aws_sdk_ec2.types.modify_traffic_mirror_filter_network_services_request.ModifyTrafficMirrorFilterNetworkServicesRequest,
) -> tuple[
    aws_sdk_ec2.types.modify_traffic_mirror_filter_network_services_result.ModifyTrafficMirrorFilterNetworkServicesResult,
    zapros.Response,
]:
    raise NotImplementedError("operation dispatch not yet generated")


async def async_modify_traffic_mirror_filter_network_services(
    options: AsyncOperationOptions,
    input: aws_sdk_ec2.types.modify_traffic_mirror_filter_network_services_request.ModifyTrafficMirrorFilterNetworkServicesRequest,
) -> tuple[
    aws_sdk_ec2.types.modify_traffic_mirror_filter_network_services_result.ModifyTrafficMirrorFilterNetworkServicesResult,
    zapros.Response,
]:
    raise NotImplementedError("operation dispatch not yet generated")
