"""Generated from Smithy shape ``com.amazonaws.ec2#EnableAwsNetworkPerformanceMetricSubscription``."""

from __future__ import annotations
from typing import TYPE_CHECKING
import zapros
import aws_sdk_ec2._auth._signers
from aws_sdk_ec2._services._pipeline import AsyncOperationOptions, OperationOptions

if TYPE_CHECKING:
    import aws_sdk_ec2.types.enable_aws_network_performance_metric_subscription_request
    import aws_sdk_ec2.types.enable_aws_network_performance_metric_subscription_result


def enable_aws_network_performance_metric_subscription(
    options: OperationOptions,
    input: aws_sdk_ec2.types.enable_aws_network_performance_metric_subscription_request.EnableAwsNetworkPerformanceMetricSubscriptionRequest,
) -> tuple[
    aws_sdk_ec2.types.enable_aws_network_performance_metric_subscription_result.EnableAwsNetworkPerformanceMetricSubscriptionResult,
    zapros.Response,
]:
    raise NotImplementedError("operation dispatch not yet generated")


async def async_enable_aws_network_performance_metric_subscription(
    options: AsyncOperationOptions,
    input: aws_sdk_ec2.types.enable_aws_network_performance_metric_subscription_request.EnableAwsNetworkPerformanceMetricSubscriptionRequest,
) -> tuple[
    aws_sdk_ec2.types.enable_aws_network_performance_metric_subscription_result.EnableAwsNetworkPerformanceMetricSubscriptionResult,
    zapros.Response,
]:
    raise NotImplementedError("operation dispatch not yet generated")
