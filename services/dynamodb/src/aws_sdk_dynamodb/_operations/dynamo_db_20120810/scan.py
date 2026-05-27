"""Generated from Smithy shape ``com.amazonaws.dynamodb#Scan``."""

from __future__ import annotations
from typing import TYPE_CHECKING
import zapros
import aws_sdk_dynamodb._auth._signers
from aws_sdk_dynamodb._services._pipeline import AsyncOperationOptions, OperationOptions

if TYPE_CHECKING:
    import aws_sdk_dynamodb.types.scan_input
    import aws_sdk_dynamodb.types.scan_output


def scan(
    options: OperationOptions, input: aws_sdk_dynamodb.types.scan_input.ScanInput
) -> tuple[aws_sdk_dynamodb.types.scan_output.ScanOutput, zapros.Response]:
    raise NotImplementedError("operation dispatch not yet generated")


async def async_scan(
    options: AsyncOperationOptions, input: aws_sdk_dynamodb.types.scan_input.ScanInput
) -> tuple[aws_sdk_dynamodb.types.scan_output.ScanOutput, zapros.Response]:
    raise NotImplementedError("operation dispatch not yet generated")
