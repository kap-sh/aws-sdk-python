"""Generated from Smithy shape ``com.amazonaws.ec2#DescribeTrafficMirrorSessions``."""

from __future__ import annotations
from typing import TYPE_CHECKING
import zapros
import aws_sdk_ec2._auth._signers
from aws_sdk_ec2._services._pipeline import AsyncOperationOptions, OperationOptions

if TYPE_CHECKING:
    import aws_sdk_ec2.types.describe_traffic_mirror_sessions_request
    import aws_sdk_ec2.types.describe_traffic_mirror_sessions_result


def describe_traffic_mirror_sessions(
    options: OperationOptions,
    input: aws_sdk_ec2.types.describe_traffic_mirror_sessions_request.DescribeTrafficMirrorSessionsRequest,
) -> tuple[
    aws_sdk_ec2.types.describe_traffic_mirror_sessions_result.DescribeTrafficMirrorSessionsResult,
    zapros.Response,
]:
    raise NotImplementedError("operation dispatch not yet generated")


async def async_describe_traffic_mirror_sessions(
    options: AsyncOperationOptions,
    input: aws_sdk_ec2.types.describe_traffic_mirror_sessions_request.DescribeTrafficMirrorSessionsRequest,
) -> tuple[
    aws_sdk_ec2.types.describe_traffic_mirror_sessions_result.DescribeTrafficMirrorSessionsResult,
    zapros.Response,
]:
    raise NotImplementedError("operation dispatch not yet generated")
