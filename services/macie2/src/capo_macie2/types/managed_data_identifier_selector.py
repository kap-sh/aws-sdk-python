"""Generated from Smithy shape ``com.amazonaws.macie2#ManagedDataIdentifierSelector``."""

from typing import Literal, TypeAlias, cast

"""<p>The selection type that determines which managed data identifiers a classification job uses to analyze data. Valid values are:</p>"""
ManagedDataIdentifierSelector: TypeAlias = Literal[
    "ALL",
    "EXCLUDE",
    "INCLUDE",
    "NONE",
    "RECOMMENDED",
]


# --- restJson1 ser/de ---
def serialize_json(value: ManagedDataIdentifierSelector) -> str:
    return value


def deserialize_json(data: str) -> ManagedDataIdentifierSelector:
    return cast(ManagedDataIdentifierSelector, data)
