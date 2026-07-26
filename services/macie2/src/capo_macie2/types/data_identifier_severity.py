"""Generated from Smithy shape ``com.amazonaws.macie2#DataIdentifierSeverity``."""

from typing import Literal, TypeAlias, cast

"""<p>The severity of a finding, ranging from LOW, for least severe, to HIGH, for most severe. Valid values are:</p>"""
DataIdentifierSeverity: TypeAlias = Literal[
    "LOW",
    "MEDIUM",
    "HIGH",
]


# --- restJson1 ser/de ---
def serialize_json(value: DataIdentifierSeverity) -> str:
    return value


def deserialize_json(data: str) -> DataIdentifierSeverity:
    return cast(DataIdentifierSeverity, data)
