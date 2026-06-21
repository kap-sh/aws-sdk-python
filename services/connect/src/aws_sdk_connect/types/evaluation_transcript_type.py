"""Generated from Smithy shape ``com.amazonaws.connect#EvaluationTranscriptType``."""

from typing import Literal, TypeAlias, cast

EvaluationTranscriptType: TypeAlias = Literal[
    "RAW",
    "REDACTED",
]


# --- restJson1 ser/de ---
def serialize_json(value: EvaluationTranscriptType) -> str:
    return value


def deserialize_json(data: str) -> EvaluationTranscriptType:
    return cast(EvaluationTranscriptType, data)
