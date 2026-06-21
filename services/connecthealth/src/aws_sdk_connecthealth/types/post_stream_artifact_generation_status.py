"""Generated from Smithy shape ``com.amazonaws.connecthealth#PostStreamArtifactGenerationStatus``."""

from typing import Literal, TypeAlias, cast

PostStreamArtifactGenerationStatus: TypeAlias = Literal[
    "IN_PROGRESS",
    "FAILED",
    "COMPLETED",
]


# --- restJson1 ser/de ---
def serialize_json(value: PostStreamArtifactGenerationStatus) -> str:
    return value


def deserialize_json(data: str) -> PostStreamArtifactGenerationStatus:
    return cast(PostStreamArtifactGenerationStatus, data)
