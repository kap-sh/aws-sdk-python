"""Generated from Smithy shape ``com.amazonaws.dynamodb#ListExports``."""

from __future__ import annotations
from typing import TYPE_CHECKING
import zapros
import aws_sdk_dynamodb._auth._signers
from aws_sdk_dynamodb._services._pipeline import AsyncOperationOptions, OperationOptions

if TYPE_CHECKING:
    import aws_sdk_dynamodb.types.list_exports_input
    import aws_sdk_dynamodb.types.list_exports_output


def list_exports(
    options: OperationOptions,
    input: aws_sdk_dynamodb.types.list_exports_input.ListExportsInput,
) -> tuple[
    aws_sdk_dynamodb.types.list_exports_output.ListExportsOutput, zapros.Response
]:
    raise NotImplementedError("operation dispatch not yet generated")


async def async_list_exports(
    options: AsyncOperationOptions,
    input: aws_sdk_dynamodb.types.list_exports_input.ListExportsInput,
) -> tuple[
    aws_sdk_dynamodb.types.list_exports_output.ListExportsOutput, zapros.Response
]:
    raise NotImplementedError("operation dispatch not yet generated")
