"""Generated from Smithy shape ``com.amazonaws.ec2#RestoreSnapshotTier``."""

from __future__ import annotations
from typing import TYPE_CHECKING
import zapros
import aws_sdk_ec2._auth._signers
from aws_sdk_ec2._services._pipeline import AsyncOperationOptions, OperationOptions

if TYPE_CHECKING:
    import aws_sdk_ec2.types.restore_snapshot_tier_request
    import aws_sdk_ec2.types.restore_snapshot_tier_result


def restore_snapshot_tier(
    options: OperationOptions,
    input: aws_sdk_ec2.types.restore_snapshot_tier_request.RestoreSnapshotTierRequest,
) -> tuple[
    aws_sdk_ec2.types.restore_snapshot_tier_result.RestoreSnapshotTierResult,
    zapros.Response,
]:
    raise NotImplementedError("operation dispatch not yet generated")


async def async_restore_snapshot_tier(
    options: AsyncOperationOptions,
    input: aws_sdk_ec2.types.restore_snapshot_tier_request.RestoreSnapshotTierRequest,
) -> tuple[
    aws_sdk_ec2.types.restore_snapshot_tier_result.RestoreSnapshotTierResult,
    zapros.Response,
]:
    raise NotImplementedError("operation dispatch not yet generated")
