"""Generated from Smithy shape ``com.amazonaws.ec2#CreateTrafficMirrorTarget``."""

from __future__ import annotations
from typing import TYPE_CHECKING
import zapros
import aws_sdk_ec2._auth._signers
from aws_sdk_ec2._services._pipeline import AsyncOperationOptions, OperationOptions

if TYPE_CHECKING:
    import aws_sdk_ec2.types.create_traffic_mirror_target_request
    import aws_sdk_ec2.types.create_traffic_mirror_target_result


def create_traffic_mirror_target(
    options: OperationOptions,
    input: aws_sdk_ec2.types.create_traffic_mirror_target_request.CreateTrafficMirrorTargetRequest,
) -> tuple[
    aws_sdk_ec2.types.create_traffic_mirror_target_result.CreateTrafficMirrorTargetResult,
    zapros.Response,
]:
    raise NotImplementedError("operation dispatch not yet generated")


async def async_create_traffic_mirror_target(
    options: AsyncOperationOptions,
    input: aws_sdk_ec2.types.create_traffic_mirror_target_request.CreateTrafficMirrorTargetRequest,
) -> tuple[
    aws_sdk_ec2.types.create_traffic_mirror_target_result.CreateTrafficMirrorTargetResult,
    zapros.Response,
]:
    raise NotImplementedError("operation dispatch not yet generated")
