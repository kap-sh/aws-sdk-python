"""Generated from Smithy shape ``com.amazonaws.lexmodelsv2#AssociatedTranscriptFilterName``."""

from typing import Literal, TypeAlias, cast

from aws_sdk_lex_models_v2.errors import DeserializationError

AssociatedTranscriptFilterName: TypeAlias = Literal[
    "IntentId",
    "SlotTypeId",
]


# --- restJson1 ser/de ---
_VALUES: frozenset[str] = frozenset(
    (
        "IntentId",
        "SlotTypeId",
    )
)


def serialize_json(value: AssociatedTranscriptFilterName) -> str:
    return value


def deserialize_json(data: str) -> AssociatedTranscriptFilterName:
    if data not in _VALUES:
        raise DeserializationError(
            f"unknown AssociatedTranscriptFilterName value: {data!r}"
        )
    return cast(AssociatedTranscriptFilterName, data)
