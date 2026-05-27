"""Generated from Smithy shape ``com.amazonaws.ec2#ImportSnapshot``."""

from __future__ import annotations
from typing import TYPE_CHECKING
import zapros
import aws_sdk_ec2._auth._signers
from aws_sdk_ec2._services._pipeline import AsyncOperationOptions, OperationOptions

if TYPE_CHECKING:
    import aws_sdk_ec2.types.import_snapshot_request
    import aws_sdk_ec2.types.import_snapshot_result


def import_snapshot(
    options: OperationOptions,
    input: aws_sdk_ec2.types.import_snapshot_request.ImportSnapshotRequest,
) -> tuple[
    aws_sdk_ec2.types.import_snapshot_result.ImportSnapshotResult, zapros.Response
]:
    raise NotImplementedError("operation dispatch not yet generated")


async def async_import_snapshot(
    options: AsyncOperationOptions,
    input: aws_sdk_ec2.types.import_snapshot_request.ImportSnapshotRequest,
) -> tuple[
    aws_sdk_ec2.types.import_snapshot_result.ImportSnapshotResult, zapros.Response
]:
    raise NotImplementedError("operation dispatch not yet generated")
