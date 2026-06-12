"""Generated from Smithy shape ``com.amazonaws.costexplorer#AnomalyFeedbackType``."""

from typing import Literal, TypeAlias, cast

from aws_sdk_cost_explorer.errors import DeserializationError

AnomalyFeedbackType: TypeAlias = Literal[
    "YES",
    "NO",
    "PLANNED_ACTIVITY",
]


# --- awsJson1_1 ser/de ---
_VALUES: frozenset[str] = frozenset(
    (
        "YES",
        "NO",
        "PLANNED_ACTIVITY",
    )
)


def serialize_aws_json_1_1(value: AnomalyFeedbackType) -> str:
    return value


def deserialize_aws_json_1_1(data: str) -> AnomalyFeedbackType:
    if data not in _VALUES:
        raise DeserializationError(f"unknown AnomalyFeedbackType value: {data!r}")
    return cast(AnomalyFeedbackType, data)
