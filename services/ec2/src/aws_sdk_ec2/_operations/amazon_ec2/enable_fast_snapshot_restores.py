"""Generated from Smithy shape ``com.amazonaws.ec2#EnableFastSnapshotRestores``."""

from __future__ import annotations
from typing import TYPE_CHECKING
import zapros
import aws_sdk_ec2._auth._signers
from aws_sdk_ec2._services._pipeline import AsyncOperationOptions, OperationOptions

if TYPE_CHECKING:
    import aws_sdk_ec2.types.enable_fast_snapshot_restores_request
    import aws_sdk_ec2.types.enable_fast_snapshot_restores_result


def enable_fast_snapshot_restores(
    options: OperationOptions,
    input: aws_sdk_ec2.types.enable_fast_snapshot_restores_request.EnableFastSnapshotRestoresRequest,
) -> tuple[
    aws_sdk_ec2.types.enable_fast_snapshot_restores_result.EnableFastSnapshotRestoresResult,
    zapros.Response,
]:
    raise NotImplementedError("operation dispatch not yet generated")


async def async_enable_fast_snapshot_restores(
    options: AsyncOperationOptions,
    input: aws_sdk_ec2.types.enable_fast_snapshot_restores_request.EnableFastSnapshotRestoresRequest,
) -> tuple[
    aws_sdk_ec2.types.enable_fast_snapshot_restores_result.EnableFastSnapshotRestoresResult,
    zapros.Response,
]:
    raise NotImplementedError("operation dispatch not yet generated")
