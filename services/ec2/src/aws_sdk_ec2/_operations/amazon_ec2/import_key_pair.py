"""Generated from Smithy shape ``com.amazonaws.ec2#ImportKeyPair``."""

from __future__ import annotations
from typing import TYPE_CHECKING
import zapros
import aws_sdk_ec2._auth._signers
from aws_sdk_ec2._services._pipeline import AsyncOperationOptions, OperationOptions

if TYPE_CHECKING:
    import aws_sdk_ec2.types.import_key_pair_request
    import aws_sdk_ec2.types.import_key_pair_result


def import_key_pair(
    options: OperationOptions,
    input: aws_sdk_ec2.types.import_key_pair_request.ImportKeyPairRequest,
) -> tuple[
    aws_sdk_ec2.types.import_key_pair_result.ImportKeyPairResult, zapros.Response
]:
    raise NotImplementedError("operation dispatch not yet generated")


async def async_import_key_pair(
    options: AsyncOperationOptions,
    input: aws_sdk_ec2.types.import_key_pair_request.ImportKeyPairRequest,
) -> tuple[
    aws_sdk_ec2.types.import_key_pair_result.ImportKeyPairResult, zapros.Response
]:
    raise NotImplementedError("operation dispatch not yet generated")
