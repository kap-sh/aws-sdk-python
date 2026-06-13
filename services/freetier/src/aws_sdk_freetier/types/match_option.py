"""Generated from Smithy shape ``com.amazonaws.freetier#MatchOption``."""

from typing import Literal, TypeAlias, cast

from aws_sdk_freetier.errors import DeserializationError

MatchOption: TypeAlias = Literal[
    "EQUALS",
    "STARTS_WITH",
    "ENDS_WITH",
    "CONTAINS",
    "GREATER_THAN_OR_EQUAL",
]


# --- awsJson1_0 ser/de ---
_VALUES: frozenset[str] = frozenset(
    (
        "EQUALS",
        "STARTS_WITH",
        "ENDS_WITH",
        "CONTAINS",
        "GREATER_THAN_OR_EQUAL",
    )
)


def serialize_aws_json_1_0(value: MatchOption) -> str:
    return value


def deserialize_aws_json_1_0(data: str) -> MatchOption:
    if data not in _VALUES:
        raise DeserializationError(f"unknown MatchOption value: {data!r}")
    return cast(MatchOption, data)
