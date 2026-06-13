"""Generated from Smithy shape ``com.amazonaws.keyspacesstreams#GetShardIteratorOutput``."""

from typing import TYPE_CHECKING, TypedDict

from typing_extensions import NotRequired

if TYPE_CHECKING:
    import aws_sdk_keyspacesstreams.types.shard_iterator


class GetShardIteratorOutput(TypedDict):
    shard_iterator: NotRequired[
        "aws_sdk_keyspacesstreams.types.shard_iterator.ShardIterator"
    ]
    """<p> The unique identifier for the shard iterator. This value is used in the <code>GetRecords</code> operation to retrieve data records from the specified shard. Each shard iterator expires 15 minutes after it is returned to the requester. </p>"""


# --- awsJson1_0 ser/de ---
def serialize_aws_json_1_0(value: GetShardIteratorOutput) -> dict:
    out: dict = {}
    if "shard_iterator" in value:
        out["shardIterator"] = value["shard_iterator"]
    return out


def deserialize_aws_json_1_0(data: dict) -> GetShardIteratorOutput:
    out: GetShardIteratorOutput = {}  # type: ignore[typeddict-item]
    if "shardIterator" in data:
        out["shard_iterator"] = data["shardIterator"]
    return out
