"""Generated from Smithy shape ``com.amazonaws.glue#JoinType``."""

from typing import Literal, TypeAlias, cast

from aws_sdk_glue.errors import DeserializationError

JoinType: TypeAlias = Literal[
    "equijoin",
    "left",
    "right",
    "outer",
    "leftsemi",
    "leftanti",
]


# --- awsJson1_1 ser/de ---
_VALUES: frozenset[str] = frozenset(
    (
        "equijoin",
        "left",
        "right",
        "outer",
        "leftsemi",
        "leftanti",
    )
)


def serialize_aws_json_1_1(value: JoinType) -> str:
    return value


def deserialize_aws_json_1_1(data: str) -> JoinType:
    if data not in _VALUES:
        raise DeserializationError(f"unknown JoinType value: {data!r}")
    return cast(JoinType, data)
