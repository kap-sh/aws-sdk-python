"""Generated from Smithy shape ``com.amazonaws.waf#PositionalConstraint``."""

from typing import Literal, TypeAlias, cast

from aws_sdk_waf.errors import DeserializationError

PositionalConstraint: TypeAlias = Literal[
    "EXACTLY",
    "STARTS_WITH",
    "ENDS_WITH",
    "CONTAINS",
    "CONTAINS_WORD",
]


# --- awsJson1_1 ser/de ---
_VALUES: frozenset[str] = frozenset(
    (
        "EXACTLY",
        "STARTS_WITH",
        "ENDS_WITH",
        "CONTAINS",
        "CONTAINS_WORD",
    )
)


def serialize_aws_json_1_1(value: PositionalConstraint) -> str:
    return value


def deserialize_aws_json_1_1(data: str) -> PositionalConstraint:
    if data not in _VALUES:
        raise DeserializationError(f"unknown PositionalConstraint value: {data!r}")
    return cast(PositionalConstraint, data)
