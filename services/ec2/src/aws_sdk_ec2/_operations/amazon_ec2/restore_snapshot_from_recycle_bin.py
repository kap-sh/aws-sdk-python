"""Generated from Smithy shape ``com.amazonaws.ec2#RestoreSnapshotFromRecycleBin``."""

from __future__ import annotations
from typing import TYPE_CHECKING
import zapros
import aws_sdk_ec2._auth._signers
from aws_sdk_ec2._services._pipeline import AsyncOperationOptions, OperationOptions

if TYPE_CHECKING:
    import aws_sdk_ec2.types.restore_snapshot_from_recycle_bin_request
    import aws_sdk_ec2.types.restore_snapshot_from_recycle_bin_result


def restore_snapshot_from_recycle_bin(
    options: OperationOptions,
    input: aws_sdk_ec2.types.restore_snapshot_from_recycle_bin_request.RestoreSnapshotFromRecycleBinRequest,
) -> tuple[
    aws_sdk_ec2.types.restore_snapshot_from_recycle_bin_result.RestoreSnapshotFromRecycleBinResult,
    zapros.Response,
]:
    raise NotImplementedError("operation dispatch not yet generated")


async def async_restore_snapshot_from_recycle_bin(
    options: AsyncOperationOptions,
    input: aws_sdk_ec2.types.restore_snapshot_from_recycle_bin_request.RestoreSnapshotFromRecycleBinRequest,
) -> tuple[
    aws_sdk_ec2.types.restore_snapshot_from_recycle_bin_result.RestoreSnapshotFromRecycleBinResult,
    zapros.Response,
]:
    raise NotImplementedError("operation dispatch not yet generated")
