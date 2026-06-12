"""Generated from Smithy shape ``com.amazonaws.macie2#SeverityDescription``."""

from typing import Literal, TypeAlias, cast

from aws_sdk_macie2.errors import DeserializationError

"""<p>The qualitative representation of the finding's severity. Possible values are:</p>"""
SeverityDescription: TypeAlias = Literal[
    "Low",
    "Medium",
    "High",
]


# --- restJson1 ser/de ---
_VALUES: frozenset[str] = frozenset(
    (
        "Low",
        "Medium",
        "High",
    )
)


def serialize_json(value: SeverityDescription) -> str:
    return value


def deserialize_json(data: str) -> SeverityDescription:
    if data not in _VALUES:
        raise DeserializationError(f"unknown SeverityDescription value: {data!r}")
    return cast(SeverityDescription, data)
