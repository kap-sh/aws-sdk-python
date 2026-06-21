"""Generated from Smithy shape ``com.amazonaws.bedrock#AutomatedReasoningCheckResult``."""

from typing import Literal, TypeAlias, cast

AutomatedReasoningCheckResult: TypeAlias = Literal[
    "VALID",
    "INVALID",
    "SATISFIABLE",
    "IMPOSSIBLE",
    "TRANSLATION_AMBIGUOUS",
    "TOO_COMPLEX",
    "NO_TRANSLATION",
]


# --- restJson1 ser/de ---
def serialize_json(value: AutomatedReasoningCheckResult) -> str:
    return value


def deserialize_json(data: str) -> AutomatedReasoningCheckResult:
    return cast(AutomatedReasoningCheckResult, data)
