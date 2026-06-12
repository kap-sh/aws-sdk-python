"""Generated from Smithy shape ``com.amazonaws.macie2#DataIdentifierSeverity``."""

from typing import Literal, TypeAlias, cast

from aws_sdk_macie2.errors import DeserializationError

"""<p>The severity of a finding, ranging from LOW, for least severe, to HIGH, for most severe. Valid values are:</p>"""
DataIdentifierSeverity: TypeAlias = Literal[
    "LOW",
    "MEDIUM",
    "HIGH",
]


# --- restJson1 ser/de ---
_VALUES: frozenset[str] = frozenset(
    (
        "LOW",
        "MEDIUM",
        "HIGH",
    )
)


def serialize_json(value: DataIdentifierSeverity) -> str:
    return value


def deserialize_json(data: str) -> DataIdentifierSeverity:
    if data not in _VALUES:
        raise DeserializationError(f"unknown DataIdentifierSeverity value: {data!r}")
    return cast(DataIdentifierSeverity, data)
