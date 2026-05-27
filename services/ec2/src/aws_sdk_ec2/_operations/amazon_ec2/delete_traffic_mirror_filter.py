"""Generated from Smithy shape ``com.amazonaws.ec2#DeleteTrafficMirrorFilter``."""

from __future__ import annotations
from typing import TYPE_CHECKING
import zapros
import aws_sdk_ec2._auth._signers
from aws_sdk_ec2._services._pipeline import AsyncOperationOptions, OperationOptions

if TYPE_CHECKING:
    import aws_sdk_ec2.types.delete_traffic_mirror_filter_request
    import aws_sdk_ec2.types.delete_traffic_mirror_filter_result


def delete_traffic_mirror_filter(
    options: OperationOptions,
    input: aws_sdk_ec2.types.delete_traffic_mirror_filter_request.DeleteTrafficMirrorFilterRequest,
) -> tuple[
    aws_sdk_ec2.types.delete_traffic_mirror_filter_result.DeleteTrafficMirrorFilterResult,
    zapros.Response,
]:
    raise NotImplementedError("operation dispatch not yet generated")


async def async_delete_traffic_mirror_filter(
    options: AsyncOperationOptions,
    input: aws_sdk_ec2.types.delete_traffic_mirror_filter_request.DeleteTrafficMirrorFilterRequest,
) -> tuple[
    aws_sdk_ec2.types.delete_traffic_mirror_filter_result.DeleteTrafficMirrorFilterResult,
    zapros.Response,
]:
    raise NotImplementedError("operation dispatch not yet generated")
