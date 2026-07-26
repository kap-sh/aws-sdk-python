"""Generated from Smithy shape ``com.amazonaws.securityagent#ArtifactType``."""

from typing import Literal, TypeAlias, cast

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
def serialize_json(value: ArtifactType) -> str:
    return value


def deserialize_json(data: str) -> ArtifactType:
    return cast(ArtifactType, data)
