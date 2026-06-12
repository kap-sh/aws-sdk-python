"""Generated from Smithy shape ``com.amazonaws.macie2#ScopeFilterKey``."""

from typing import Literal, TypeAlias, cast

from aws_sdk_macie2.errors import DeserializationError

"""<p>The property to use in a condition that determines whether an S3 object is included or excluded from a classification job. Valid values are:</p>"""
ScopeFilterKey: TypeAlias = Literal[
    "OBJECT_EXTENSION",
    "OBJECT_LAST_MODIFIED_DATE",
    "OBJECT_SIZE",
    "OBJECT_KEY",
]


# --- restJson1 ser/de ---
_VALUES: frozenset[str] = frozenset(
    (
        "OBJECT_EXTENSION",
        "OBJECT_LAST_MODIFIED_DATE",
        "OBJECT_SIZE",
        "OBJECT_KEY",
    )
)


def serialize_json(value: ScopeFilterKey) -> str:
    return value


def deserialize_json(data: str) -> ScopeFilterKey:
    if data not in _VALUES:
        raise DeserializationError(f"unknown ScopeFilterKey value: {data!r}")
    return cast(ScopeFilterKey, data)
