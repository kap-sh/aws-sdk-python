"""Generated from Smithy shape ``com.amazonaws.ec2#CreateSnapshots``."""

from __future__ import annotations
from typing import TYPE_CHECKING
import zapros
import aws_sdk_ec2._auth._signers
from aws_sdk_ec2._services._pipeline import AsyncOperationOptions, OperationOptions

if TYPE_CHECKING:
    import aws_sdk_ec2.types.create_snapshots_request
    import aws_sdk_ec2.types.create_snapshots_result


def create_snapshots(
    options: OperationOptions,
    input: aws_sdk_ec2.types.create_snapshots_request.CreateSnapshotsRequest,
) -> tuple[
    aws_sdk_ec2.types.create_snapshots_result.CreateSnapshotsResult, zapros.Response
]:
    raise NotImplementedError("operation dispatch not yet generated")


async def async_create_snapshots(
    options: AsyncOperationOptions,
    input: aws_sdk_ec2.types.create_snapshots_request.CreateSnapshotsRequest,
) -> tuple[
    aws_sdk_ec2.types.create_snapshots_result.CreateSnapshotsResult, zapros.Response
]:
    raise NotImplementedError("operation dispatch not yet generated")
