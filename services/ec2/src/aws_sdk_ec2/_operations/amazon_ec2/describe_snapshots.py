"""Generated from Smithy shape ``com.amazonaws.ec2#DescribeSnapshots``."""

from __future__ import annotations
from typing import TYPE_CHECKING
import zapros
import aws_sdk_ec2._auth._signers
from aws_sdk_ec2._services._pipeline import AsyncOperationOptions, OperationOptions

if TYPE_CHECKING:
    import aws_sdk_ec2.types.describe_snapshots_request
    import aws_sdk_ec2.types.describe_snapshots_result


def describe_snapshots(
    options: OperationOptions,
    input: aws_sdk_ec2.types.describe_snapshots_request.DescribeSnapshotsRequest,
) -> tuple[
    aws_sdk_ec2.types.describe_snapshots_result.DescribeSnapshotsResult, zapros.Response
]:
    raise NotImplementedError("operation dispatch not yet generated")


async def async_describe_snapshots(
    options: AsyncOperationOptions,
    input: aws_sdk_ec2.types.describe_snapshots_request.DescribeSnapshotsRequest,
) -> tuple[
    aws_sdk_ec2.types.describe_snapshots_result.DescribeSnapshotsResult, zapros.Response
]:
    raise NotImplementedError("operation dispatch not yet generated")
