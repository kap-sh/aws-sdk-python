"""Generated from Smithy shape ``com.amazonaws.forecast#FilterConditionString``."""

from typing import Literal, TypeAlias, cast

from aws_sdk_forecast.errors import DeserializationError

FilterConditionString: TypeAlias = Literal[
    "IS",
    "IS_NOT",
]


# --- awsJson1_1 ser/de ---
_VALUES: frozenset[str] = frozenset(
    (
        "IS",
        "IS_NOT",
    )
)


def serialize_aws_json_1_1(value: FilterConditionString) -> str:
    return value


def deserialize_aws_json_1_1(data: str) -> FilterConditionString:
    if data not in _VALUES:
        raise DeserializationError(f"unknown FilterConditionString value: {data!r}")
    return cast(FilterConditionString, data)
