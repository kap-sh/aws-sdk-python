"""Generated from Smithy shape ``com.amazonaws.macie2#ScopeFilterKey``."""

from typing import Literal, TypeAlias, cast

"""<p>The property to use in a condition that determines whether an S3 object is included or excluded from a classification job. Valid values are:</p>"""
ScopeFilterKey: TypeAlias = Literal[
    "OBJECT_EXTENSION",
    "OBJECT_LAST_MODIFIED_DATE",
    "OBJECT_SIZE",
    "OBJECT_KEY",
]


# --- restJson1 ser/de ---
def serialize_json(value: ScopeFilterKey) -> str:
    return value


def deserialize_json(data: str) -> ScopeFilterKey:
    return cast(ScopeFilterKey, data)
