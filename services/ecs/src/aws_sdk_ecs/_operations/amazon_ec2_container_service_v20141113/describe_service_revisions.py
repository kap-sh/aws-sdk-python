"""Generated from Smithy shape ``com.amazonaws.ecs#DescribeServiceRevisions``."""

from __future__ import annotations
from typing import TYPE_CHECKING
import zapros
import aws_sdk_ecs._auth._signers
from aws_sdk_ecs._services._pipeline import AsyncOperationOptions, OperationOptions

if TYPE_CHECKING:
    import aws_sdk_ecs.types.describe_service_revisions_request
    import aws_sdk_ecs.types.describe_service_revisions_response


def describe_service_revisions(
    options: OperationOptions,
    input: aws_sdk_ecs.types.describe_service_revisions_request.DescribeServiceRevisionsRequest,
) -> tuple[
    aws_sdk_ecs.types.describe_service_revisions_response.DescribeServiceRevisionsResponse,
    zapros.Response,
]:
    raise NotImplementedError("operation dispatch not yet generated")


async def async_describe_service_revisions(
    options: AsyncOperationOptions,
    input: aws_sdk_ecs.types.describe_service_revisions_request.DescribeServiceRevisionsRequest,
) -> tuple[
    aws_sdk_ecs.types.describe_service_revisions_response.DescribeServiceRevisionsResponse,
    zapros.Response,
]:
    raise NotImplementedError("operation dispatch not yet generated")
