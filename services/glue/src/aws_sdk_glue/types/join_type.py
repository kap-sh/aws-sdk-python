"""Generated from Smithy shape ``com.amazonaws.glue#JoinType``."""

from typing import Literal, TypeAlias, cast

JoinType: TypeAlias = Literal[
    "equijoin",
    "left",
    "right",
    "outer",
    "leftsemi",
    "leftanti",
]


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: JoinType) -> str:
    return value


def deserialize_aws_json_1_1(data: str) -> JoinType:
    return cast(JoinType, data)
