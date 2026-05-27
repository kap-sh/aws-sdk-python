"""Generated from Smithy shape ``com.amazonaws.ec2#DescribeAwsNetworkPerformanceMetricSubscriptions``."""

from __future__ import annotations
from typing import TYPE_CHECKING
import zapros
import aws_sdk_ec2._auth._signers
from aws_sdk_ec2._services._pipeline import AsyncOperationOptions, OperationOptions

if TYPE_CHECKING:
    import aws_sdk_ec2.types.describe_aws_network_performance_metric_subscriptions_request
    import aws_sdk_ec2.types.describe_aws_network_performance_metric_subscriptions_result


def describe_aws_network_performance_metric_subscriptions(
    options: OperationOptions,
    input: aws_sdk_ec2.types.describe_aws_network_performance_metric_subscriptions_request.DescribeAwsNetworkPerformanceMetricSubscriptionsRequest,
) -> tuple[
    aws_sdk_ec2.types.describe_aws_network_performance_metric_subscriptions_result.DescribeAwsNetworkPerformanceMetricSubscriptionsResult,
    zapros.Response,
]:
    raise NotImplementedError("operation dispatch not yet generated")


async def async_describe_aws_network_performance_metric_subscriptions(
    options: AsyncOperationOptions,
    input: aws_sdk_ec2.types.describe_aws_network_performance_metric_subscriptions_request.DescribeAwsNetworkPerformanceMetricSubscriptionsRequest,
) -> tuple[
    aws_sdk_ec2.types.describe_aws_network_performance_metric_subscriptions_result.DescribeAwsNetworkPerformanceMetricSubscriptionsResult,
    zapros.Response,
]:
    raise NotImplementedError("operation dispatch not yet generated")
