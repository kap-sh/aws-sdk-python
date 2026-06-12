"""Generated from Smithy shape ``com.amazonaws.kendra#Order``."""

from typing import Literal, TypeAlias, cast

from aws_sdk_kendra.errors import DeserializationError

Order: TypeAlias = Literal[
    "ASCENDING",
    "DESCENDING",
]


# --- awsJson1_1 ser/de ---
_VALUES: frozenset[str] = frozenset(
    (
        "ASCENDING",
        "DESCENDING",
    )
)


def serialize_aws_json_1_1(value: Order) -> str:
    return value


def deserialize_aws_json_1_1(data: str) -> Order:
    if data not in _VALUES:
        raise DeserializationError(f"unknown Order value: {data!r}")
    return cast(Order, data)
