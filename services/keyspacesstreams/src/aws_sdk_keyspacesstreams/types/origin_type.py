"""Generated from Smithy shape ``com.amazonaws.keyspacesstreams#OriginType``."""

from typing import Literal, TypeAlias, cast

OriginType: TypeAlias = Literal[
    "USER",
    "REPLICATION",
    "TTL",
]


# --- awsJson1_0 ser/de ---
def serialize_aws_json_1_0(value: OriginType) -> str:
    return value


def deserialize_aws_json_1_0(data: str) -> OriginType:
    return cast(OriginType, data)
