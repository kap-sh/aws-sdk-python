"""Generated from Smithy shape ``com.amazonaws.dynamodb#ListImports``."""

from __future__ import annotations
from typing import TYPE_CHECKING
import zapros
import aws_sdk_dynamodb._auth._signers
from aws_sdk_dynamodb._services._pipeline import AsyncOperationOptions, OperationOptions

if TYPE_CHECKING:
    import aws_sdk_dynamodb.types.list_imports_input
    import aws_sdk_dynamodb.types.list_imports_output


def list_imports(
    options: OperationOptions,
    input: aws_sdk_dynamodb.types.list_imports_input.ListImportsInput,
) -> tuple[
    aws_sdk_dynamodb.types.list_imports_output.ListImportsOutput, zapros.Response
]:
    raise NotImplementedError("operation dispatch not yet generated")


async def async_list_imports(
    options: AsyncOperationOptions,
    input: aws_sdk_dynamodb.types.list_imports_input.ListImportsInput,
) -> tuple[
    aws_sdk_dynamodb.types.list_imports_output.ListImportsOutput, zapros.Response
]:
    raise NotImplementedError("operation dispatch not yet generated")
