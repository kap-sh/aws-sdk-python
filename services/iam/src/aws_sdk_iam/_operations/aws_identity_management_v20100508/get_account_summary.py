"""Generated from Smithy shape ``com.amazonaws.iam#GetAccountSummary``."""

from __future__ import annotations
from typing import TYPE_CHECKING
import zapros
import aws_sdk_iam._auth._signers
from aws_sdk_iam._services._pipeline import AsyncOperationOptions, OperationOptions

if TYPE_CHECKING:
    import aws_sdk_iam.types.get_account_summary_response


def get_account_summary(
    options: OperationOptions,
) -> tuple[
    aws_sdk_iam.types.get_account_summary_response.GetAccountSummaryResponse,
    zapros.Response,
]:
    raise NotImplementedError("operation dispatch not yet generated")


async def async_get_account_summary(
    options: AsyncOperationOptions,
) -> tuple[
    aws_sdk_iam.types.get_account_summary_response.GetAccountSummaryResponse,
    zapros.Response,
]:
    raise NotImplementedError("operation dispatch not yet generated")
