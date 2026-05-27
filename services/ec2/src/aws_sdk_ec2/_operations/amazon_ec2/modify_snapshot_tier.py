"""Generated from Smithy shape ``com.amazonaws.ec2#ModifySnapshotTier``."""

from __future__ import annotations
from typing import TYPE_CHECKING
import zapros
import aws_sdk_ec2._auth._signers
from aws_sdk_ec2._services._pipeline import AsyncOperationOptions, OperationOptions

if TYPE_CHECKING:
    import aws_sdk_ec2.types.modify_snapshot_tier_request
    import aws_sdk_ec2.types.modify_snapshot_tier_result


def modify_snapshot_tier(
    options: OperationOptions,
    input: aws_sdk_ec2.types.modify_snapshot_tier_request.ModifySnapshotTierRequest,
) -> tuple[
    aws_sdk_ec2.types.modify_snapshot_tier_result.ModifySnapshotTierResult,
    zapros.Response,
]:
    raise NotImplementedError("operation dispatch not yet generated")


async def async_modify_snapshot_tier(
    options: AsyncOperationOptions,
    input: aws_sdk_ec2.types.modify_snapshot_tier_request.ModifySnapshotTierRequest,
) -> tuple[
    aws_sdk_ec2.types.modify_snapshot_tier_result.ModifySnapshotTierResult,
    zapros.Response,
]:
    raise NotImplementedError("operation dispatch not yet generated")
