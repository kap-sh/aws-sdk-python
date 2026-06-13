"""Generated from Smithy shape ``com.amazonaws.quicksight#ComparisonMethodType``."""

from typing import Literal, TypeAlias, cast

from aws_sdk_quicksight.errors import DeserializationError

ComparisonMethodType: TypeAlias = Literal[
    "DIFF",
    "PERC_DIFF",
    "DIFF_AS_PERC",
    "POP_CURRENT_DIFF_AS_PERC",
    "POP_CURRENT_DIFF",
    "POP_OVERTIME_DIFF_AS_PERC",
    "POP_OVERTIME_DIFF",
    "PERCENT_OF_TOTAL",
    "RUNNING_SUM",
    "MOVING_AVERAGE",
]


# --- restJson1 ser/de ---
_VALUES: frozenset[str] = frozenset(
    (
        "DIFF",
        "PERC_DIFF",
        "DIFF_AS_PERC",
        "POP_CURRENT_DIFF_AS_PERC",
        "POP_CURRENT_DIFF",
        "POP_OVERTIME_DIFF_AS_PERC",
        "POP_OVERTIME_DIFF",
        "PERCENT_OF_TOTAL",
        "RUNNING_SUM",
        "MOVING_AVERAGE",
    )
)


def serialize_json(value: ComparisonMethodType) -> str:
    return value


def deserialize_json(data: str) -> ComparisonMethodType:
    if data not in _VALUES:
        raise DeserializationError(f"unknown ComparisonMethodType value: {data!r}")
    return cast(ComparisonMethodType, data)
