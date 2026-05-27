"""Generated from Smithy shape ``com.amazonaws.ec2#UnlockSnapshot``."""

from __future__ import annotations
from typing import TYPE_CHECKING
import zapros
import aws_sdk_ec2._auth._signers
from aws_sdk_ec2._services._pipeline import AsyncOperationOptions, OperationOptions

if TYPE_CHECKING:
    import aws_sdk_ec2.types.unlock_snapshot_request
    import aws_sdk_ec2.types.unlock_snapshot_result


def unlock_snapshot(
    options: OperationOptions,
    input: aws_sdk_ec2.types.unlock_snapshot_request.UnlockSnapshotRequest,
) -> tuple[
    aws_sdk_ec2.types.unlock_snapshot_result.UnlockSnapshotResult, zapros.Response
]:
    raise NotImplementedError("operation dispatch not yet generated")


async def async_unlock_snapshot(
    options: AsyncOperationOptions,
    input: aws_sdk_ec2.types.unlock_snapshot_request.UnlockSnapshotRequest,
) -> tuple[
    aws_sdk_ec2.types.unlock_snapshot_result.UnlockSnapshotResult, zapros.Response
]:
    raise NotImplementedError("operation dispatch not yet generated")
