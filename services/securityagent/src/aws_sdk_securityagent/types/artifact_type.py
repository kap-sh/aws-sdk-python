"""Generated from Smithy shape ``com.amazonaws.securityagent#ArtifactType``."""

from typing import Literal, TypeAlias, cast

from aws_sdk_securityagent.errors import DeserializationError

"""<p>Supported file extension types for artifacts.</p>"""
ArtifactType: TypeAlias = Literal[
    "TXT",
    "PNG",
    "JPEG",
    "MD",
    "PDF",
    "DOCX",
    "DOC",
    "JSON",
    "YAML",
]


# --- restJson1 ser/de ---
_VALUES: frozenset[str] = frozenset(
    (
        "TXT",
        "PNG",
        "JPEG",
        "MD",
        "PDF",
        "DOCX",
        "DOC",
        "JSON",
        "YAML",
    )
)


def serialize_json(value: ArtifactType) -> str:
    return value


def deserialize_json(data: str) -> ArtifactType:
    if data not in _VALUES:
        raise DeserializationError(f"unknown ArtifactType value: {data!r}")
    return cast(ArtifactType, data)
