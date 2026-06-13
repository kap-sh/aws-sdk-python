"""Generated from Smithy shape ``com.amazonaws.taxsettings#ChileDocumentType``."""

from typing import Literal, TypeAlias, cast

from aws_sdk_taxsettings.errors import DeserializationError

"""<p> The type of tax document for Chile.</p>"""
ChileDocumentType: TypeAlias = Literal[
    "Invoice",
    "Receipt",
]


# --- restJson1 ser/de ---
_VALUES: frozenset[str] = frozenset(
    (
        "Invoice",
        "Receipt",
    )
)


def serialize_json(value: ChileDocumentType) -> str:
    return value


def deserialize_json(data: str) -> ChileDocumentType:
    if data not in _VALUES:
        raise DeserializationError(f"unknown ChileDocumentType value: {data!r}")
    return cast(ChileDocumentType, data)
