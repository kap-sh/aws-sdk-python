"""Generated from Smithy shape ``com.amazonaws.keyspacesstreams#ShardFilterType``."""

from typing import Literal, TypeAlias, cast

ShardFilterType: TypeAlias = Literal["CHILD_SHARDS",]


# --- awsJson1_0 ser/de ---
def serialize_aws_json_1_0(value: ShardFilterType) -> str:
    return value


def deserialize_aws_json_1_0(data: str) -> ShardFilterType:
    return cast(ShardFilterType, data)
