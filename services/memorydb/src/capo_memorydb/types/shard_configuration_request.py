"""Generated from Smithy shape ``com.amazonaws.memorydb#ShardConfigurationRequest``."""

from typing import TYPE_CHECKING

from typing_extensions import TypedDict

if TYPE_CHECKING:
    import capo_memorydb.types.integer


class ShardConfigurationRequest(TypedDict, closed=True):
    shard_count: "capo_memorydb.types.integer.Integer"
    """<p>The number of shards in the cluster</p>"""


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: ShardConfigurationRequest) -> dict:
    out: dict = {}
    out["ShardCount"] = value.get("shard_count", 0)
    return out


def deserialize_aws_json_1_1(data: dict) -> ShardConfigurationRequest:
    out: ShardConfigurationRequest = {}  # type: ignore[typeddict-item]
    if "ShardCount" in data:
        out["shard_count"] = data["ShardCount"]
    else:
        out["shard_count"] = 0
    return out
