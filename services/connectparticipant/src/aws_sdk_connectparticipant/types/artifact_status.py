"""Generated from Smithy shape ``com.amazonaws.connectparticipant#ArtifactStatus``."""

from typing import Literal, TypeAlias, cast

from aws_sdk_connectparticipant.errors import DeserializationError

ArtifactStatus: TypeAlias = Literal[
    "APPROVED",
    "REJECTED",
    "IN_PROGRESS",
]


# --- restJson1 ser/de ---
_VALUES: frozenset[str] = frozenset(
    (
        "APPROVED",
        "REJECTED",
        "IN_PROGRESS",
    )
)


def serialize_json(value: ArtifactStatus) -> str:
    return value


def deserialize_json(data: str) -> ArtifactStatus:
    if data not in _VALUES:
        raise DeserializationError(f"unknown ArtifactStatus value: {data!r}")
    return cast(ArtifactStatus, data)
