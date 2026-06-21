"""Generated from Smithy shape ``com.amazonaws.storagegateway#PoolStatus``."""

from typing import Literal, TypeAlias, cast

PoolStatus: TypeAlias = Literal[
    "ACTIVE",
    "DELETED",
]


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: PoolStatus) -> str:
    return value


def deserialize_aws_json_1_1(data: str) -> PoolStatus:
    return cast(PoolStatus, data)
