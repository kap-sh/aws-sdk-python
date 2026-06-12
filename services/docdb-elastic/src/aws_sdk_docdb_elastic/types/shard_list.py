"""Generated from Smithy shape ``com.amazonaws.docdbelastic#ShardList``."""

from typing import TYPE_CHECKING, TypeAlias

if TYPE_CHECKING:
    import aws_sdk_docdb_elastic.types.shard

ShardList: TypeAlias = list["aws_sdk_docdb_elastic.types.shard.Shard"]


# --- restJson1 ser/de ---
def serialize_json(value: ShardList) -> list:
    import aws_sdk_docdb_elastic.types.shard

    out: list = []
    for item in value:
        out.append(aws_sdk_docdb_elastic.types.shard.serialize_json(item))
    return out


def deserialize_json(data: list) -> ShardList:
    import aws_sdk_docdb_elastic.types.shard

    out: ShardList = []
    for item in data:
        out.append(aws_sdk_docdb_elastic.types.shard.deserialize_json(item))
    return out
