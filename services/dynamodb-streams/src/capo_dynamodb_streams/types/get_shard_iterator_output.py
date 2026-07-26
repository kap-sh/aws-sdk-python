"""Generated from Smithy shape ``com.amazonaws.dynamodbstreams#GetShardIteratorOutput``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import capo_dynamodb_streams.types.shard_iterator


class GetShardIteratorOutput(TypedDict, closed=True):
    shard_iterator: NotRequired[
        "capo_dynamodb_streams.types.shard_iterator.ShardIterator"
    ]
    """<p>The position in the shard from which to start reading stream records sequentially. A shard iterator specifies this position using the sequence number of a stream record in a shard.</p>"""


# --- awsJson1_0 ser/de ---
def serialize_aws_json_1_0(value: GetShardIteratorOutput) -> dict:
    out: dict = {}
    if "shard_iterator" in value:
        out["ShardIterator"] = value["shard_iterator"]
    return out


def deserialize_aws_json_1_0(data: dict) -> GetShardIteratorOutput:
    out: GetShardIteratorOutput = {}  # type: ignore[typeddict-item]
    if "ShardIterator" in data:
        out["shard_iterator"] = data["ShardIterator"]
    return out
