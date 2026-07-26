"""Generated from Smithy shape ``com.amazonaws.qconnect#SpanFinishReasonList``."""

from typing import TYPE_CHECKING, TypeAlias

if TYPE_CHECKING:
    import capo_qconnect.types.non_empty_string

SpanFinishReasonList: TypeAlias = list[
    "capo_qconnect.types.non_empty_string.NonEmptyString"
]


# --- restJson1 ser/de ---
def serialize_json(value: SpanFinishReasonList) -> list:
    return list(value)


def deserialize_json(data: list) -> SpanFinishReasonList:
    return list(data)
