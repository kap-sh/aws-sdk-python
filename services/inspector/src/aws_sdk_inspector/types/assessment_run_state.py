"""Generated from Smithy shape ``com.amazonaws.inspector#AssessmentRunState``."""

from typing import Literal, TypeAlias, cast

from aws_sdk_inspector.errors import DeserializationError

AssessmentRunState: TypeAlias = Literal[
    "CREATED",
    "START_DATA_COLLECTION_PENDING",
    "START_DATA_COLLECTION_IN_PROGRESS",
    "COLLECTING_DATA",
    "STOP_DATA_COLLECTION_PENDING",
    "DATA_COLLECTED",
    "START_EVALUATING_RULES_PENDING",
    "EVALUATING_RULES",
    "FAILED",
    "ERROR",
    "COMPLETED",
    "COMPLETED_WITH_ERRORS",
    "CANCELED",
]


# --- awsJson1_1 ser/de ---
_VALUES: frozenset[str] = frozenset(
    (
        "CREATED",
        "START_DATA_COLLECTION_PENDING",
        "START_DATA_COLLECTION_IN_PROGRESS",
        "COLLECTING_DATA",
        "STOP_DATA_COLLECTION_PENDING",
        "DATA_COLLECTED",
        "START_EVALUATING_RULES_PENDING",
        "EVALUATING_RULES",
        "FAILED",
        "ERROR",
        "COMPLETED",
        "COMPLETED_WITH_ERRORS",
        "CANCELED",
    )
)


def serialize_aws_json_1_1(value: AssessmentRunState) -> str:
    return value


def deserialize_aws_json_1_1(data: str) -> AssessmentRunState:
    if data not in _VALUES:
        raise DeserializationError(f"unknown AssessmentRunState value: {data!r}")
    return cast(AssessmentRunState, data)
