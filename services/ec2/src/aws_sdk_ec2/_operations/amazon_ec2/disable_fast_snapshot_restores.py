"""Generated from Smithy shape ``com.amazonaws.ec2#DisableFastSnapshotRestores``."""

from __future__ import annotations
from typing import TYPE_CHECKING
import zapros
import aws_sdk_ec2._auth._signers
from aws_sdk_ec2._services._pipeline import AsyncOperationOptions, OperationOptions

if TYPE_CHECKING:
    import aws_sdk_ec2.types.disable_fast_snapshot_restores_request
    import aws_sdk_ec2.types.disable_fast_snapshot_restores_result


def disable_fast_snapshot_restores(
    options: OperationOptions,
    input: aws_sdk_ec2.types.disable_fast_snapshot_restores_request.DisableFastSnapshotRestoresRequest,
) -> tuple[
    aws_sdk_ec2.types.disable_fast_snapshot_restores_result.DisableFastSnapshotRestoresResult,
    zapros.Response,
]:
    raise NotImplementedError("operation dispatch not yet generated")


async def async_disable_fast_snapshot_restores(
    options: AsyncOperationOptions,
    input: aws_sdk_ec2.types.disable_fast_snapshot_restores_request.DisableFastSnapshotRestoresRequest,
) -> tuple[
    aws_sdk_ec2.types.disable_fast_snapshot_restores_result.DisableFastSnapshotRestoresResult,
    zapros.Response,
]:
    raise NotImplementedError("operation dispatch not yet generated")
