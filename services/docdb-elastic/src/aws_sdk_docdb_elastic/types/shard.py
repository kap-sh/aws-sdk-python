"""Generated from Smithy shape ``com.amazonaws.docdbelastic#Shard``."""

from typing import TYPE_CHECKING

from typing_extensions import TypedDict

from aws_sdk_docdb_elastic.errors import DeserializationError

if TYPE_CHECKING:
    import aws_sdk_docdb_elastic.types.status


class Shard(TypedDict, closed=True):
    shard_id: "str"
    """<p>The ID of the shard.</p>"""
    create_time: "str"
    """<p>The time when the shard was created in Universal Coordinated Time (UTC).</p>"""
    status: "aws_sdk_docdb_elastic.types.status.Status"
    """<p>The current status of the shard.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: Shard) -> dict:
    out: dict = {}
    out["shardId"] = value["shard_id"]
    out["createTime"] = value["create_time"]
    out["status"] = value["status"]
    return out


def deserialize_json(data: dict) -> Shard:
    out: Shard = {}  # type: ignore[typeddict-item]
    if "shardId" in data:
        out["shard_id"] = data["shardId"]
    else:
        raise DeserializationError("Shard.shard_id required")
    if "createTime" in data:
        out["create_time"] = data["createTime"]
    else:
        raise DeserializationError("Shard.create_time required")
    if "status" in data:
        out["status"] = data["status"]
    else:
        raise DeserializationError("Shard.status required")
    return out
