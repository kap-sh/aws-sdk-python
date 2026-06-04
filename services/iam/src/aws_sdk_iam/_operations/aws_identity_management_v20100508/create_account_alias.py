"""Generated from Smithy shape ``com.amazonaws.iam#CreateAccountAlias``."""

from __future__ import annotations
from typing import TYPE_CHECKING
import zapros
import aws_sdk_iam._auth._signers
from aws_sdk_iam._services._pipeline import AsyncOperationOptions, OperationOptions

if TYPE_CHECKING:
    import aws_sdk_iam.types.create_account_alias_request


def create_account_alias(
    options: OperationOptions,
    input: aws_sdk_iam.types.create_account_alias_request.CreateAccountAliasRequest,
) -> tuple[None, zapros.Response]:
    raise NotImplementedError("operation dispatch not yet generated")


async def async_create_account_alias(
    options: AsyncOperationOptions,
    input: aws_sdk_iam.types.create_account_alias_request.CreateAccountAliasRequest,
) -> tuple[None, zapros.Response]:
    raise NotImplementedError("operation dispatch not yet generated")
