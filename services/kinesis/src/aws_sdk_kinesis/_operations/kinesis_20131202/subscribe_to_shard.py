"""Generated from Smithy shape ``com.amazonaws.kinesis#SubscribeToShard``."""

from __future__ import annotations

from typing import TYPE_CHECKING

import zapros

from aws_sdk_kinesis._services._pipeline import AsyncOperationOptions, OperationOptions

if TYPE_CHECKING:
    import aws_sdk_kinesis.types.subscribe_to_shard_input
    import aws_sdk_kinesis.types.subscribe_to_shard_output


def subscribe_to_shard(
    options: OperationOptions,
    input: aws_sdk_kinesis.types.subscribe_to_shard_input.SubscribeToShardInput,
) -> tuple[
    aws_sdk_kinesis.types.subscribe_to_shard_output.SubscribeToShardOutput,
    zapros.Response,
]:
    raise NotImplementedError("event stream output is not yet supported")


async def async_subscribe_to_shard(
    options: AsyncOperationOptions,
    input: aws_sdk_kinesis.types.subscribe_to_shard_input.SubscribeToShardInput,
) -> tuple[
    aws_sdk_kinesis.types.subscribe_to_shard_output.SubscribeToShardOutput,
    zapros.Response,
]:
    raise NotImplementedError("event stream output is not yet supported")
