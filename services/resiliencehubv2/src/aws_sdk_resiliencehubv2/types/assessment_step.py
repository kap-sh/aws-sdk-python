"""Generated from Smithy shape ``com.amazonaws.resiliencehubv2#AssessmentStep``."""

from typing import Literal, TypeAlias, cast

from aws_sdk_resiliencehubv2.errors import DeserializationError

AssessmentStep: TypeAlias = Literal[
    "TOPOLOGY_ENHANCEMENT",
    "SERVICE_FUNCTION_GENERATION",
    "RESILIENCE_ASSESSMENT",
]


# --- restJson1 ser/de ---
_VALUES: frozenset[str] = frozenset(
    (
        "TOPOLOGY_ENHANCEMENT",
        "SERVICE_FUNCTION_GENERATION",
        "RESILIENCE_ASSESSMENT",
    )
)


def serialize_json(value: AssessmentStep) -> str:
    return value


def deserialize_json(data: str) -> AssessmentStep:
    if data not in _VALUES:
        raise DeserializationError(f"unknown AssessmentStep value: {data!r}")
    return cast(AssessmentStep, data)
