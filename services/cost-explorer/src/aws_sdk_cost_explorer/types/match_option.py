"""Generated from Smithy shape ``com.amazonaws.costexplorer#MatchOption``."""

from typing import Literal, TypeAlias, cast

from aws_sdk_cost_explorer.errors import DeserializationError

MatchOption: TypeAlias = Literal[
    "EQUALS",
    "ABSENT",
    "STARTS_WITH",
    "ENDS_WITH",
    "CONTAINS",
    "CASE_SENSITIVE",
    "CASE_INSENSITIVE",
    "GREATER_THAN_OR_EQUAL",
]


# --- awsJson1_1 ser/de ---
_VALUES: frozenset[str] = frozenset(
    (
        "EQUALS",
        "ABSENT",
        "STARTS_WITH",
        "ENDS_WITH",
        "CONTAINS",
        "CASE_SENSITIVE",
        "CASE_INSENSITIVE",
        "GREATER_THAN_OR_EQUAL",
    )
)


def serialize_aws_json_1_1(value: MatchOption) -> str:
    return value


def deserialize_aws_json_1_1(data: str) -> MatchOption:
    if data not in _VALUES:
        raise DeserializationError(f"unknown MatchOption value: {data!r}")
    return cast(MatchOption, data)
