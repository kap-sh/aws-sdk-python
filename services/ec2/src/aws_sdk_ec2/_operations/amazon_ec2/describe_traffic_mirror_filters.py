"""Generated from Smithy shape ``com.amazonaws.ec2#DescribeTrafficMirrorFilters``."""

from __future__ import annotations
from typing import TYPE_CHECKING
import zapros
import aws_sdk_ec2._auth._signers
from aws_sdk_ec2._services._pipeline import AsyncOperationOptions, OperationOptions

if TYPE_CHECKING:
    import aws_sdk_ec2.types.describe_traffic_mirror_filters_request
    import aws_sdk_ec2.types.describe_traffic_mirror_filters_result


def describe_traffic_mirror_filters(
    options: OperationOptions,
    input: aws_sdk_ec2.types.describe_traffic_mirror_filters_request.DescribeTrafficMirrorFiltersRequest,
) -> tuple[
    aws_sdk_ec2.types.describe_traffic_mirror_filters_result.DescribeTrafficMirrorFiltersResult,
    zapros.Response,
]:
    raise NotImplementedError("operation dispatch not yet generated")


async def async_describe_traffic_mirror_filters(
    options: AsyncOperationOptions,
    input: aws_sdk_ec2.types.describe_traffic_mirror_filters_request.DescribeTrafficMirrorFiltersRequest,
) -> tuple[
    aws_sdk_ec2.types.describe_traffic_mirror_filters_result.DescribeTrafficMirrorFiltersResult,
    zapros.Response,
]:
    raise NotImplementedError("operation dispatch not yet generated")
