"""Generated from Smithy shape ``com.amazonaws.docdbelastic#ShardList``."""

from typing import TYPE_CHECKING, TypeAlias

if TYPE_CHECKING:
    import capo_docdb_elastic.types.shard

ShardList: TypeAlias = list["capo_docdb_elastic.types.shard.Shard"]


# --- restJson1 ser/de ---
def serialize_json(value: ShardList) -> list:
    import capo_docdb_elastic.types.shard

    out: list = []
    for item in value:
        out.append(capo_docdb_elastic.types.shard.serialize_json(item))
    return out


def deserialize_json(data: list) -> ShardList:
    import capo_docdb_elastic.types.shard

    out: ShardList = []
    for item in data:
        out.append(capo_docdb_elastic.types.shard.deserialize_json(item))
    return out
