"""Generated from Smithy shape ``com.amazonaws.taxsettings#ChileDocumentType``."""

from typing import Literal, TypeAlias, cast

"""<p> The type of tax document for Chile.</p>"""
ChileDocumentType: TypeAlias = Literal[
    "Invoice",
    "Receipt",
]


# --- restJson1 ser/de ---
def serialize_json(value: ChileDocumentType) -> str:
    return value


def deserialize_json(data: str) -> ChileDocumentType:
    return cast(ChileDocumentType, data)
