"""Generated from Smithy shape ``com.amazonaws.ec2#CreateSnapshot``."""

from __future__ import annotations
from typing import TYPE_CHECKING
import zapros
import aws_sdk_ec2._auth._signers
from aws_sdk_ec2._services._pipeline import AsyncOperationOptions, OperationOptions

if TYPE_CHECKING:
    import aws_sdk_ec2.types.create_snapshot_request
    import aws_sdk_ec2.types.snapshot


def create_snapshot(
    options: OperationOptions,
    input: aws_sdk_ec2.types.create_snapshot_request.CreateSnapshotRequest,
) -> tuple[aws_sdk_ec2.types.snapshot.Snapshot, zapros.Response]:
    raise NotImplementedError("operation dispatch not yet generated")


async def async_create_snapshot(
    options: AsyncOperationOptions,
    input: aws_sdk_ec2.types.create_snapshot_request.CreateSnapshotRequest,
) -> tuple[aws_sdk_ec2.types.snapshot.Snapshot, zapros.Response]:
    raise NotImplementedError("operation dispatch not yet generated")
