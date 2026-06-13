"""Generated from Smithy shape ``com.amazonaws.bedrockruntime#DocumentFormat``."""

from typing import Literal, TypeAlias, cast

from aws_sdk_bedrock_runtime.errors import DeserializationError

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
_VALUES: frozenset[str] = frozenset(
    (
        "pdf",
        "csv",
        "doc",
        "docx",
        "xls",
        "xlsx",
        "html",
        "txt",
        "md",
    )
)


def serialize_json(value: DocumentFormat) -> str:
    return value


def deserialize_json(data: str) -> DocumentFormat:
    if data not in _VALUES:
        raise DeserializationError(f"unknown DocumentFormat value: {data!r}")
    return cast(DocumentFormat, data)
