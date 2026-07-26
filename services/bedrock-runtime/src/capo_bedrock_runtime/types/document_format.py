"""Generated from Smithy shape ``com.amazonaws.bedrockruntime#DocumentFormat``."""

from typing import Literal, TypeAlias, cast

DocumentFormat: TypeAlias = Literal[
    "pdf",
    "csv",
    "doc",
    "docx",
    "xls",
    "xlsx",
    "html",
    "txt",
    "md",
]


# --- restJson1 ser/de ---
def serialize_json(value: DocumentFormat) -> str:
    return value


def deserialize_json(data: str) -> DocumentFormat:
    return cast(DocumentFormat, data)
