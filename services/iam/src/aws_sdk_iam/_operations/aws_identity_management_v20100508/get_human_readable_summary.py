"""Generated from Smithy shape ``com.amazonaws.iam#GetHumanReadableSummary``."""

from __future__ import annotations
from typing import TYPE_CHECKING
import zapros
import aws_sdk_iam._auth._signers
from aws_sdk_iam._services._pipeline import AsyncOperationOptions, OperationOptions

if TYPE_CHECKING:
    import aws_sdk_iam.types.get_human_readable_summary_request
    import aws_sdk_iam.types.get_human_readable_summary_response


def get_human_readable_summary(
    options: OperationOptions,
    input: aws_sdk_iam.types.get_human_readable_summary_request.GetHumanReadableSummaryRequest,
) -> tuple[
    aws_sdk_iam.types.get_human_readable_summary_response.GetHumanReadableSummaryResponse,
    zapros.Response,
]:
    raise NotImplementedError("operation dispatch not yet generated")


async def async_get_human_readable_summary(
    options: AsyncOperationOptions,
    input: aws_sdk_iam.types.get_human_readable_summary_request.GetHumanReadableSummaryRequest,
) -> tuple[
    aws_sdk_iam.types.get_human_readable_summary_response.GetHumanReadableSummaryResponse,
    zapros.Response,
]:
    raise NotImplementedError("operation dispatch not yet generated")
