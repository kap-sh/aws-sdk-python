"""Generated from Smithy shape ``com.amazonaws.ec2#CreateTrafficMirrorFilter``."""

from __future__ import annotations
from typing import TYPE_CHECKING
import zapros
import aws_sdk_ec2._auth._signers
from aws_sdk_ec2._services._pipeline import AsyncOperationOptions, OperationOptions

if TYPE_CHECKING:
    import aws_sdk_ec2.types.create_traffic_mirror_filter_request
    import aws_sdk_ec2.types.create_traffic_mirror_filter_result


def create_traffic_mirror_filter(
    options: OperationOptions,
    input: aws_sdk_ec2.types.create_traffic_mirror_filter_request.CreateTrafficMirrorFilterRequest,
) -> tuple[
    aws_sdk_ec2.types.create_traffic_mirror_filter_result.CreateTrafficMirrorFilterResult,
    zapros.Response,
]:
    raise NotImplementedError("operation dispatch not yet generated")


async def async_create_traffic_mirror_filter(
    options: AsyncOperationOptions,
    input: aws_sdk_ec2.types.create_traffic_mirror_filter_request.CreateTrafficMirrorFilterRequest,
) -> tuple[
    aws_sdk_ec2.types.create_traffic_mirror_filter_result.CreateTrafficMirrorFilterResult,
    zapros.Response,
]:
    raise NotImplementedError("operation dispatch not yet generated")
