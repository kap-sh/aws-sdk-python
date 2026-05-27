"""Generated from Smithy shape ``com.amazonaws.dynamodb#UpdateTableReplicaAutoScaling``."""

from __future__ import annotations
from typing import TYPE_CHECKING
import zapros
import aws_sdk_dynamodb._auth._signers
from aws_sdk_dynamodb._services._pipeline import AsyncOperationOptions, OperationOptions

if TYPE_CHECKING:
    import aws_sdk_dynamodb.types.update_table_replica_auto_scaling_input
    import aws_sdk_dynamodb.types.update_table_replica_auto_scaling_output


def update_table_replica_auto_scaling(
    options: OperationOptions,
    input: aws_sdk_dynamodb.types.update_table_replica_auto_scaling_input.UpdateTableReplicaAutoScalingInput,
) -> tuple[
    aws_sdk_dynamodb.types.update_table_replica_auto_scaling_output.UpdateTableReplicaAutoScalingOutput,
    zapros.Response,
]:
    raise NotImplementedError("operation dispatch not yet generated")


async def async_update_table_replica_auto_scaling(
    options: AsyncOperationOptions,
    input: aws_sdk_dynamodb.types.update_table_replica_auto_scaling_input.UpdateTableReplicaAutoScalingInput,
) -> tuple[
    aws_sdk_dynamodb.types.update_table_replica_auto_scaling_output.UpdateTableReplicaAutoScalingOutput,
    zapros.Response,
]:
    raise NotImplementedError("operation dispatch not yet generated")
