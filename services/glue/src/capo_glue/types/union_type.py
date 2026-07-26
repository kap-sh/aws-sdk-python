"""Generated from Smithy shape ``com.amazonaws.glue#UnionType``."""

from typing import Literal, TypeAlias, cast

UnionType: TypeAlias = Literal[
    "ALL",
    "DISTINCT",
]


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: UnionType) -> str:
    return value


def deserialize_aws_json_1_1(data: str) -> UnionType:
    return cast(UnionType, data)
