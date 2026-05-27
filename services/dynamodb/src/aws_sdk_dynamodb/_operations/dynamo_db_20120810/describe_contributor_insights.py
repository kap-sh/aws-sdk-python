"""Generated from Smithy shape ``com.amazonaws.dynamodb#DescribeContributorInsights``."""

from __future__ import annotations
from typing import TYPE_CHECKING
import zapros
import aws_sdk_dynamodb._auth._signers
from aws_sdk_dynamodb._services._pipeline import AsyncOperationOptions, OperationOptions

if TYPE_CHECKING:
    import aws_sdk_dynamodb.types.describe_contributor_insights_input
    import aws_sdk_dynamodb.types.describe_contributor_insights_output


def describe_contributor_insights(
    options: OperationOptions,
    input: aws_sdk_dynamodb.types.describe_contributor_insights_input.DescribeContributorInsightsInput,
) -> tuple[
    aws_sdk_dynamodb.types.describe_contributor_insights_output.DescribeContributorInsightsOutput,
    zapros.Response,
]:
    raise NotImplementedError("operation dispatch not yet generated")


async def async_describe_contributor_insights(
    options: AsyncOperationOptions,
    input: aws_sdk_dynamodb.types.describe_contributor_insights_input.DescribeContributorInsightsInput,
) -> tuple[
    aws_sdk_dynamodb.types.describe_contributor_insights_output.DescribeContributorInsightsOutput,
    zapros.Response,
]:
    raise NotImplementedError("operation dispatch not yet generated")
