"""Generated from Smithy shape ``com.amazonaws.inspector#InspectorEvent``."""

from typing import Literal, TypeAlias, cast

from aws_sdk_inspector.errors import DeserializationError

InspectorEvent: TypeAlias = Literal[
    "ASSESSMENT_RUN_STARTED",
    "ASSESSMENT_RUN_COMPLETED",
    "ASSESSMENT_RUN_STATE_CHANGED",
    "FINDING_REPORTED",
    "OTHER",
]


# --- awsJson1_1 ser/de ---
_VALUES: frozenset[str] = frozenset(
    (
        "ASSESSMENT_RUN_STARTED",
        "ASSESSMENT_RUN_COMPLETED",
        "ASSESSMENT_RUN_STATE_CHANGED",
        "FINDING_REPORTED",
        "OTHER",
    )
)


def serialize_aws_json_1_1(value: InspectorEvent) -> str:
    return value


def deserialize_aws_json_1_1(data: str) -> InspectorEvent:
    if data not in _VALUES:
        raise DeserializationError(f"unknown InspectorEvent value: {data!r}")
    return cast(InspectorEvent, data)
