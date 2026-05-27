"""Generated from Smithy shape ``com.amazonaws.ec2#CreateSpotDatafeedSubscription``."""

from __future__ import annotations
from typing import TYPE_CHECKING
import zapros
import aws_sdk_ec2._auth._signers
from aws_sdk_ec2._services._pipeline import AsyncOperationOptions, OperationOptions

if TYPE_CHECKING:
    import aws_sdk_ec2.types.create_spot_datafeed_subscription_request
    import aws_sdk_ec2.types.create_spot_datafeed_subscription_result


def create_spot_datafeed_subscription(
    options: OperationOptions,
    input: aws_sdk_ec2.types.create_spot_datafeed_subscription_request.CreateSpotDatafeedSubscriptionRequest,
) -> tuple[
    aws_sdk_ec2.types.create_spot_datafeed_subscription_result.CreateSpotDatafeedSubscriptionResult,
    zapros.Response,
]:
    raise NotImplementedError("operation dispatch not yet generated")


async def async_create_spot_datafeed_subscription(
    options: AsyncOperationOptions,
    input: aws_sdk_ec2.types.create_spot_datafeed_subscription_request.CreateSpotDatafeedSubscriptionRequest,
) -> tuple[
    aws_sdk_ec2.types.create_spot_datafeed_subscription_result.CreateSpotDatafeedSubscriptionResult,
    zapros.Response,
]:
    raise NotImplementedError("operation dispatch not yet generated")
