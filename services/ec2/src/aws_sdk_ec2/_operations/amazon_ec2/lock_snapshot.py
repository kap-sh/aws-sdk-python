"""Generated from Smithy shape ``com.amazonaws.ec2#LockSnapshot``."""

from __future__ import annotations
from typing import TYPE_CHECKING
import zapros
import aws_sdk_ec2._auth._signers
from aws_sdk_ec2._services._pipeline import AsyncOperationOptions, OperationOptions

if TYPE_CHECKING:
    import aws_sdk_ec2.types.lock_snapshot_request
    import aws_sdk_ec2.types.lock_snapshot_result


def lock_snapshot(
    options: OperationOptions,
    input: aws_sdk_ec2.types.lock_snapshot_request.LockSnapshotRequest,
) -> tuple[aws_sdk_ec2.types.lock_snapshot_result.LockSnapshotResult, zapros.Response]:
    raise NotImplementedError("operation dispatch not yet generated")


async def async_lock_snapshot(
    options: AsyncOperationOptions,
    input: aws_sdk_ec2.types.lock_snapshot_request.LockSnapshotRequest,
) -> tuple[aws_sdk_ec2.types.lock_snapshot_result.LockSnapshotResult, zapros.Response]:
    raise NotImplementedError("operation dispatch not yet generated")
