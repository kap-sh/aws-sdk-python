"""Generated from Smithy shape ``com.amazonaws.costexplorer#TermInYears``."""

from typing import Literal, TypeAlias, cast

from aws_sdk_cost_explorer.errors import DeserializationError

TermInYears: TypeAlias = Literal[
    "ONE_YEAR",
    "THREE_YEARS",
]


# --- awsJson1_1 ser/de ---
_VALUES: frozenset[str] = frozenset(
    (
        "ONE_YEAR",
        "THREE_YEARS",
    )
)


def serialize_aws_json_1_1(value: TermInYears) -> str:
    return value


def deserialize_aws_json_1_1(data: str) -> TermInYears:
    if data not in _VALUES:
        raise DeserializationError(f"unknown TermInYears value: {data!r}")
    return cast(TermInYears, data)
