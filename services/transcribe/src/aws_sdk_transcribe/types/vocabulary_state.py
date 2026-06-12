"""Generated from Smithy shape ``com.amazonaws.transcribe#VocabularyState``."""

from typing import Literal, TypeAlias, cast

from aws_sdk_transcribe.errors import DeserializationError

VocabularyState: TypeAlias = Literal[
    "PENDING",
    "READY",
    "FAILED",
]


# --- awsJson1_1 ser/de ---
_VALUES: frozenset[str] = frozenset(
    (
        "PENDING",
        "READY",
        "FAILED",
    )
)


def serialize_aws_json_1_1(value: VocabularyState) -> str:
    return value


def deserialize_aws_json_1_1(data: str) -> VocabularyState:
    if data not in _VALUES:
        raise DeserializationError(f"unknown VocabularyState value: {data!r}")
    return cast(VocabularyState, data)
