"""Generated from Smithy shape ``com.amazonaws.macie2#RetrievalMode``."""

from typing import Literal, TypeAlias, cast

"""<p>The access method to use when retrieving occurrences of sensitive data reported by findings. Valid values are:</p>"""
RetrievalMode: TypeAlias = Literal[
    "CALLER_CREDENTIALS",
    "ASSUME_ROLE",
]


# --- restJson1 ser/de ---
def serialize_json(value: RetrievalMode) -> str:
    return value


def deserialize_json(data: str) -> RetrievalMode:
    return cast(RetrievalMode, data)
