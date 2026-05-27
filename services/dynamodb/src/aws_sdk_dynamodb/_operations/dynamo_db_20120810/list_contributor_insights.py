"""Generated from Smithy shape ``com.amazonaws.dynamodb#ListContributorInsights``."""

from __future__ import annotations
from typing import TYPE_CHECKING
import zapros
import aws_sdk_dynamodb._auth._signers
from aws_sdk_dynamodb._services._pipeline import AsyncOperationOptions, OperationOptions

if TYPE_CHECKING:
    import aws_sdk_dynamodb.types.list_contributor_insights_input
    import aws_sdk_dynamodb.types.list_contributor_insights_output


def list_contributor_insights(
    options: OperationOptions,
    input: aws_sdk_dynamodb.types.list_contributor_insights_input.ListContributorInsightsInput,
) -> tuple[
    aws_sdk_dynamodb.types.list_contributor_insights_output.ListContributorInsightsOutput,
    zapros.Response,
]:
    raise NotImplementedError("operation dispatch not yet generated")


async def async_list_contributor_insights(
    options: AsyncOperationOptions,
    input: aws_sdk_dynamodb.types.list_contributor_insights_input.ListContributorInsightsInput,
) -> tuple[
    aws_sdk_dynamodb.types.list_contributor_insights_output.ListContributorInsightsOutput,
    zapros.Response,
]:
    raise NotImplementedError("operation dispatch not yet generated")
