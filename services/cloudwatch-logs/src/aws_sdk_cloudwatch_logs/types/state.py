"""Generated from Smithy shape ``com.amazonaws.cloudwatchlogs#State``."""

from typing import Literal, TypeAlias, cast

from aws_sdk_cloudwatch_logs.errors import DeserializationError

State: TypeAlias = Literal[
    "Active",
    "Suppressed",
    "Baseline",
]


# --- awsJson1_1 ser/de ---
_VALUES: frozenset[str] = frozenset(
    (
        "Active",
        "Suppressed",
        "Baseline",
    )
)


def serialize_aws_json_1_1(value: State) -> str:
    return value


def deserialize_aws_json_1_1(data: str) -> State:
    if data not in _VALUES:
        raise DeserializationError(f"unknown State value: {data!r}")
    return cast(State, data)
