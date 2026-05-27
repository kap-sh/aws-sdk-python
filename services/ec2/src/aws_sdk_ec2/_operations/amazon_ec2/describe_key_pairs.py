"""Generated from Smithy shape ``com.amazonaws.ec2#DescribeKeyPairs``."""

from __future__ import annotations
from typing import TYPE_CHECKING
import zapros
import aws_sdk_ec2._auth._signers
from aws_sdk_ec2._services._pipeline import AsyncOperationOptions, OperationOptions

if TYPE_CHECKING:
    import aws_sdk_ec2.types.describe_key_pairs_request
    import aws_sdk_ec2.types.describe_key_pairs_result


def describe_key_pairs(
    options: OperationOptions,
    input: aws_sdk_ec2.types.describe_key_pairs_request.DescribeKeyPairsRequest,
) -> tuple[
    aws_sdk_ec2.types.describe_key_pairs_result.DescribeKeyPairsResult, zapros.Response
]:
    raise NotImplementedError("operation dispatch not yet generated")


async def async_describe_key_pairs(
    options: AsyncOperationOptions,
    input: aws_sdk_ec2.types.describe_key_pairs_request.DescribeKeyPairsRequest,
) -> tuple[
    aws_sdk_ec2.types.describe_key_pairs_result.DescribeKeyPairsResult, zapros.Response
]:
    raise NotImplementedError("operation dispatch not yet generated")
