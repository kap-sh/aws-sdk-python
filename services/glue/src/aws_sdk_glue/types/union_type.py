"""Generated from Smithy shape ``com.amazonaws.glue#UnionType``."""

from typing import Literal, TypeAlias, cast

from aws_sdk_glue.errors import DeserializationError

UnionType: TypeAlias = Literal[
    "ALL",
    "DISTINCT",
]


# --- awsJson1_1 ser/de ---
_VALUES: frozenset[str] = frozenset(
    (
        "ALL",
        "DISTINCT",
    )
)


def serialize_aws_json_1_1(value: UnionType) -> str:
    return value


def deserialize_aws_json_1_1(data: str) -> UnionType:
    if data not in _VALUES:
        raise DeserializationError(f"unknown UnionType value: {data!r}")
    return cast(UnionType, data)
