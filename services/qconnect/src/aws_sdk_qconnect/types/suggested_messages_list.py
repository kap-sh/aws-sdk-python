"""Generated from Smithy shape ``com.amazonaws.qconnect#SuggestedMessagesList``."""

from typing import TYPE_CHECKING, TypeAlias

if TYPE_CHECKING:
    import aws_sdk_qconnect.types.non_empty_sensitive_string

SuggestedMessagesList: TypeAlias = list[
    "aws_sdk_qconnect.types.non_empty_sensitive_string.NonEmptySensitiveString"
]


# --- restJson1 ser/de ---
def serialize_json(value: SuggestedMessagesList) -> list:
    return list(value)


def deserialize_json(data: list) -> SuggestedMessagesList:
    return list(data)
