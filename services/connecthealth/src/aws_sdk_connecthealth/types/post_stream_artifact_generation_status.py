"""Generated from Smithy shape ``com.amazonaws.connecthealth#PostStreamArtifactGenerationStatus``."""

from typing import Literal, TypeAlias, cast

from aws_sdk_connecthealth.errors import DeserializationError

PostStreamArtifactGenerationStatus: TypeAlias = Literal[
    "IN_PROGRESS",
    "FAILED",
    "COMPLETED",
]


# --- restJson1 ser/de ---
_VALUES: frozenset[str] = frozenset(
    (
        "IN_PROGRESS",
        "FAILED",
        "COMPLETED",
    )
)


def serialize_json(value: PostStreamArtifactGenerationStatus) -> str:
    return value


def deserialize_json(data: str) -> PostStreamArtifactGenerationStatus:
    if data not in _VALUES:
        raise DeserializationError(
            f"unknown PostStreamArtifactGenerationStatus value: {data!r}"
        )
    return cast(PostStreamArtifactGenerationStatus, data)
