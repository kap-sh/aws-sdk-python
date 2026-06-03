"""Generated from Smithy shape ``com.amazonaws.secretsmanager#RemoveRegionsFromReplication``."""

from __future__ import annotations
from typing import TYPE_CHECKING
import zapros
import aws_sdk_secrets_manager._auth._signers
from aws_sdk_secrets_manager._services._pipeline import (
    AsyncOperationOptions,
    OperationOptions,
)

if TYPE_CHECKING:
    import aws_sdk_secrets_manager.types.remove_regions_from_replication_request
    import aws_sdk_secrets_manager.types.remove_regions_from_replication_response


def remove_regions_from_replication(
    options: OperationOptions,
    input: aws_sdk_secrets_manager.types.remove_regions_from_replication_request.RemoveRegionsFromReplicationRequest,
) -> tuple[
    aws_sdk_secrets_manager.types.remove_regions_from_replication_response.RemoveRegionsFromReplicationResponse,
    zapros.Response,
]:
    raise NotImplementedError("operation dispatch not yet generated")


async def async_remove_regions_from_replication(
    options: AsyncOperationOptions,
    input: aws_sdk_secrets_manager.types.remove_regions_from_replication_request.RemoveRegionsFromReplicationRequest,
) -> tuple[
    aws_sdk_secrets_manager.types.remove_regions_from_replication_response.RemoveRegionsFromReplicationResponse,
    zapros.Response,
]:
    raise NotImplementedError("operation dispatch not yet generated")
