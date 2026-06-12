"""Generated from Smithy shape ``com.amazonaws.b2bi#X12SplitBy``."""

from typing import Literal, TypeAlias, cast

from aws_sdk_b2bi.errors import DeserializationError

X12SplitBy: TypeAlias = Literal[
    "NONE",
    "TRANSACTION",
]


# --- awsJson1_0 ser/de ---
_VALUES: frozenset[str] = frozenset(
    (
        "NONE",
        "TRANSACTION",
    )
)


def serialize_aws_json_1_0(value: X12SplitBy) -> str:
    return value


def deserialize_aws_json_1_0(data: str) -> X12SplitBy:
    if data not in _VALUES:
        raise DeserializationError(f"unknown X12SplitBy value: {data!r}")
    return cast(X12SplitBy, data)
