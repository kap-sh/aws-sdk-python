"""Generated from Smithy shape ``com.amazonaws.kinesis#GetShardIteratorOutput``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import capo_kinesis.types.shard_iterator


class GetShardIteratorOutput(TypedDict, closed=True):
    shard_iterator: NotRequired["capo_kinesis.types.shard_iterator.ShardIterator"]
    """<p>The position in the shard from which to start reading data records sequentially. A shard iterator specifies this position using the sequence number of a data record in a shard.</p>"""


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: GetShardIteratorOutput) -> dict:
    out: dict = {}
    if "shard_iterator" in value:
        out["ShardIterator"] = value["shard_iterator"]
    return out


def deserialize_aws_json_1_1(data: dict) -> GetShardIteratorOutput:
    out: GetShardIteratorOutput = {}  # type: ignore[typeddict-item]
    if "ShardIterator" in data:
        out["shard_iterator"] = data["ShardIterator"]
    return out
