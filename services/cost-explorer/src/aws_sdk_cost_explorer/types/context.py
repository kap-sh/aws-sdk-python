"""Generated from Smithy shape ``com.amazonaws.costexplorer#Context``."""

from typing import Literal, TypeAlias, cast

from aws_sdk_cost_explorer.errors import DeserializationError

Context: TypeAlias = Literal[
    "COST_AND_USAGE",
    "RESERVATIONS",
    "SAVINGS_PLANS",
]


# --- awsJson1_1 ser/de ---
_VALUES: frozenset[str] = frozenset(
    (
        "COST_AND_USAGE",
        "RESERVATIONS",
        "SAVINGS_PLANS",
    )
)


def serialize_aws_json_1_1(value: Context) -> str:
    return value


def deserialize_aws_json_1_1(data: str) -> Context:
    if data not in _VALUES:
        raise DeserializationError(f"unknown Context value: {data!r}")
    return cast(Context, data)
