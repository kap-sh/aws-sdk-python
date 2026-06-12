"""Generated from Smithy shape ``com.amazonaws.macie2#ManagedDataIdentifierSelector``."""

from typing import Literal, TypeAlias, cast

from aws_sdk_macie2.errors import DeserializationError

"""<p>The selection type that determines which managed data identifiers a classification job uses to analyze data. Valid values are:</p>"""
ManagedDataIdentifierSelector: TypeAlias = Literal[
    "ALL",
    "EXCLUDE",
    "INCLUDE",
    "NONE",
    "RECOMMENDED",
]


# --- restJson1 ser/de ---
_VALUES: frozenset[str] = frozenset(
    (
        "ALL",
        "EXCLUDE",
        "INCLUDE",
        "NONE",
        "RECOMMENDED",
    )
)


def serialize_json(value: ManagedDataIdentifierSelector) -> str:
    return value


def deserialize_json(data: str) -> ManagedDataIdentifierSelector:
    if data not in _VALUES:
        raise DeserializationError(
            f"unknown ManagedDataIdentifierSelector value: {data!r}"
        )
    return cast(ManagedDataIdentifierSelector, data)
