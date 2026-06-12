"""Generated from Smithy shape ``com.amazonaws.macie2#RetrievalMode``."""

from typing import Literal, TypeAlias, cast

from aws_sdk_macie2.errors import DeserializationError

"""<p>The access method to use when retrieving occurrences of sensitive data reported by findings. Valid values are:</p>"""
RetrievalMode: TypeAlias = Literal[
    "CALLER_CREDENTIALS",
    "ASSUME_ROLE",
]


# --- restJson1 ser/de ---
_VALUES: frozenset[str] = frozenset(
    (
        "CALLER_CREDENTIALS",
        "ASSUME_ROLE",
    )
)


def serialize_json(value: RetrievalMode) -> str:
    return value


def deserialize_json(data: str) -> RetrievalMode:
    if data not in _VALUES:
        raise DeserializationError(f"unknown RetrievalMode value: {data!r}")
    return cast(RetrievalMode, data)
