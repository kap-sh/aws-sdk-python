"""Generated from Smithy shape ``com.amazonaws.kinesis#SubscribeToShardOutput``."""

from typing import TYPE_CHECKING

from typing_extensions import TypedDict

if TYPE_CHECKING:
    import aws_sdk_kinesis.types.subscribe_to_shard_event_stream


class SubscribeToShardOutput(TypedDict, closed=True):
    event_stream: "aws_sdk_kinesis.types.subscribe_to_shard_event_stream.SubscribeToShardEventStream"
    """<p>The event stream that your consumer can use to read records from the shard.</p>"""
