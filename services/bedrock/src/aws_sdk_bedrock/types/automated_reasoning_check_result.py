"""Generated from Smithy shape ``com.amazonaws.bedrock#AutomatedReasoningCheckResult``."""

from typing import Literal, TypeAlias, cast

from aws_sdk_bedrock.errors import DeserializationError

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
_VALUES: frozenset[str] = frozenset(
    (
        "VALID",
        "INVALID",
        "SATISFIABLE",
        "IMPOSSIBLE",
        "TRANSLATION_AMBIGUOUS",
        "TOO_COMPLEX",
        "NO_TRANSLATION",
    )
)


def serialize_json(value: AutomatedReasoningCheckResult) -> str:
    return value


def deserialize_json(data: str) -> AutomatedReasoningCheckResult:
    if data not in _VALUES:
        raise DeserializationError(
            f"unknown AutomatedReasoningCheckResult value: {data!r}"
        )
    return cast(AutomatedReasoningCheckResult, data)
