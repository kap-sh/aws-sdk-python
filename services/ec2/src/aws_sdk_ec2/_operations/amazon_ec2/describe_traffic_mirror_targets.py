"""Generated from Smithy shape ``com.amazonaws.ec2#DescribeTrafficMirrorTargets``."""

from __future__ import annotations
from typing import TYPE_CHECKING
import zapros
import aws_sdk_ec2._auth._signers
from aws_sdk_ec2._services._pipeline import AsyncOperationOptions, OperationOptions

if TYPE_CHECKING:
    import aws_sdk_ec2.types.describe_traffic_mirror_targets_request
    import aws_sdk_ec2.types.describe_traffic_mirror_targets_result


def describe_traffic_mirror_targets(
    options: OperationOptions,
    input: aws_sdk_ec2.types.describe_traffic_mirror_targets_request.DescribeTrafficMirrorTargetsRequest,
) -> tuple[
    aws_sdk_ec2.types.describe_traffic_mirror_targets_result.DescribeTrafficMirrorTargetsResult,
    zapros.Response,
]:
    raise NotImplementedError("operation dispatch not yet generated")


async def async_describe_traffic_mirror_targets(
    options: AsyncOperationOptions,
    input: aws_sdk_ec2.types.describe_traffic_mirror_targets_request.DescribeTrafficMirrorTargetsRequest,
) -> tuple[
    aws_sdk_ec2.types.describe_traffic_mirror_targets_result.DescribeTrafficMirrorTargetsResult,
    zapros.Response,
]:
    raise NotImplementedError("operation dispatch not yet generated")
