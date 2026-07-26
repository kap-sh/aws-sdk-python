"""Generated from Smithy shape ``com.amazonaws.resiliencehubv2#AssessmentStep``."""

from typing import Literal, TypeAlias, cast

AssessmentStep: TypeAlias = Literal[
    "TOPOLOGY_ENHANCEMENT",
    "SERVICE_FUNCTION_GENERATION",
    "RESILIENCE_ASSESSMENT",
]


# --- restJson1 ser/de ---
def serialize_json(value: AssessmentStep) -> str:
    return value


def deserialize_json(data: str) -> AssessmentStep:
    return cast(AssessmentStep, data)
