"""Generated from Smithy shape ``com.amazonaws.ec2#EnableSnapshotBlockPublicAccess``."""

from __future__ import annotations
from typing import TYPE_CHECKING
import zapros
import aws_sdk_ec2._auth._signers
from aws_sdk_ec2._services._pipeline import AsyncOperationOptions, OperationOptions

if TYPE_CHECKING:
    import aws_sdk_ec2.types.enable_snapshot_block_public_access_request
    import aws_sdk_ec2.types.enable_snapshot_block_public_access_result


def enable_snapshot_block_public_access(
    options: OperationOptions,
    input: aws_sdk_ec2.types.enable_snapshot_block_public_access_request.EnableSnapshotBlockPublicAccessRequest,
) -> tuple[
    aws_sdk_ec2.types.enable_snapshot_block_public_access_result.EnableSnapshotBlockPublicAccessResult,
    zapros.Response,
]:
    raise NotImplementedError("operation dispatch not yet generated")


async def async_enable_snapshot_block_public_access(
    options: AsyncOperationOptions,
    input: aws_sdk_ec2.types.enable_snapshot_block_public_access_request.EnableSnapshotBlockPublicAccessRequest,
) -> tuple[
    aws_sdk_ec2.types.enable_snapshot_block_public_access_result.EnableSnapshotBlockPublicAccessResult,
    zapros.Response,
]:
    raise NotImplementedError("operation dispatch not yet generated")
