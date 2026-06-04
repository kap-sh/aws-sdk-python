"""Generated from Smithy shape ``com.amazonaws.iam#ListAccountAliases``."""

from __future__ import annotations
from typing import TYPE_CHECKING
import zapros
import aws_sdk_iam._auth._signers
from aws_sdk_iam._services._pipeline import AsyncOperationOptions, OperationOptions

if TYPE_CHECKING:
    import aws_sdk_iam.types.list_account_aliases_request
    import aws_sdk_iam.types.list_account_aliases_response


def list_account_aliases(
    options: OperationOptions,
    input: aws_sdk_iam.types.list_account_aliases_request.ListAccountAliasesRequest,
) -> tuple[
    aws_sdk_iam.types.list_account_aliases_response.ListAccountAliasesResponse,
    zapros.Response,
]:
    raise NotImplementedError("operation dispatch not yet generated")


async def async_list_account_aliases(
    options: AsyncOperationOptions,
    input: aws_sdk_iam.types.list_account_aliases_request.ListAccountAliasesRequest,
) -> tuple[
    aws_sdk_iam.types.list_account_aliases_response.ListAccountAliasesResponse,
    zapros.Response,
]:
    raise NotImplementedError("operation dispatch not yet generated")
