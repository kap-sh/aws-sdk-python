"""Generated from Smithy shape ``com.amazonaws.memorydb#FailoverShardRequest``."""

from typing import TYPE_CHECKING

from typing_extensions import TypedDict

from capo_memorydb.errors import DeserializationError

if TYPE_CHECKING:
    import capo_memorydb.types.string


class FailoverShardRequest(TypedDict, closed=True):
    cluster_name: "capo_memorydb.types.string.String"
    """<p>The cluster being failed over.</p>"""
    shard_name: "capo_memorydb.types.string.String"
    """<p>The name of the shard.</p>"""


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: FailoverShardRequest) -> dict:
    out: dict = {}
    out["ClusterName"] = value["cluster_name"]
    out["ShardName"] = value["shard_name"]
    return out


def deserialize_aws_json_1_1(data: dict) -> FailoverShardRequest:
    out: FailoverShardRequest = {}  # type: ignore[typeddict-item]
    if "ClusterName" in data:
        out["cluster_name"] = data["ClusterName"]
    else:
        raise DeserializationError("FailoverShardRequest.cluster_name required")
    if "ShardName" in data:
        out["shard_name"] = data["ShardName"]
    else:
        raise DeserializationError("FailoverShardRequest.shard_name required")
    return out
