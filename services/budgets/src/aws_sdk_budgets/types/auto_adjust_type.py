"""Generated from Smithy shape ``com.amazonaws.budgets#AutoAdjustType``."""

from typing import Literal, TypeAlias, cast

from aws_sdk_budgets.errors import DeserializationError

AutoAdjustType: TypeAlias = Literal[
    "HISTORICAL",
    "FORECAST",
]


# --- awsJson1_1 ser/de ---
_VALUES: frozenset[str] = frozenset(
    (
        "HISTORICAL",
        "FORECAST",
    )
)


def serialize_aws_json_1_1(value: AutoAdjustType) -> str:
    return value


def deserialize_aws_json_1_1(data: str) -> AutoAdjustType:
    if data not in _VALUES:
        raise DeserializationError(f"unknown AutoAdjustType value: {data!r}")
    return cast(AutoAdjustType, data)
