"""Generated from Smithy shape ``com.amazonaws.secretsmanager#StopReplicationToReplica``."""

from __future__ import annotations
from typing import TYPE_CHECKING
import zapros
import aws_sdk_secrets_manager._auth._signers
from aws_sdk_secrets_manager._services._pipeline import (
    AsyncOperationOptions,
    OperationOptions,
)

if TYPE_CHECKING:
    import aws_sdk_secrets_manager.types.stop_replication_to_replica_request
    import aws_sdk_secrets_manager.types.stop_replication_to_replica_response


def stop_replication_to_replica(
    options: OperationOptions,
    input: aws_sdk_secrets_manager.types.stop_replication_to_replica_request.StopReplicationToReplicaRequest,
) -> tuple[
    aws_sdk_secrets_manager.types.stop_replication_to_replica_response.StopReplicationToReplicaResponse,
    zapros.Response,
]:
    raise NotImplementedError("operation dispatch not yet generated")


async def async_stop_replication_to_replica(
    options: AsyncOperationOptions,
    input: aws_sdk_secrets_manager.types.stop_replication_to_replica_request.StopReplicationToReplicaRequest,
) -> tuple[
    aws_sdk_secrets_manager.types.stop_replication_to_replica_response.StopReplicationToReplicaResponse,
    zapros.Response,
]:
    raise NotImplementedError("operation dispatch not yet generated")
