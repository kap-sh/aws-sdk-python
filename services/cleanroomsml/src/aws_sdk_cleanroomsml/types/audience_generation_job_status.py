"""Generated from Smithy shape ``com.amazonaws.cleanroomsml#AudienceGenerationJobStatus``."""

from typing import Literal, TypeAlias, cast

from aws_sdk_cleanroomsml.errors import DeserializationError

AudienceGenerationJobStatus: TypeAlias = Literal[
    "CREATE_PENDING",
    "CREATE_IN_PROGRESS",
    "CREATE_FAILED",
    "ACTIVE",
    "DELETE_PENDING",
    "DELETE_IN_PROGRESS",
    "DELETE_FAILED",
]


# --- restJson1 ser/de ---
_VALUES: frozenset[str] = frozenset(
    (
        "CREATE_PENDING",
        "CREATE_IN_PROGRESS",
        "CREATE_FAILED",
        "ACTIVE",
        "DELETE_PENDING",
        "DELETE_IN_PROGRESS",
        "DELETE_FAILED",
    )
)


def serialize_json(value: AudienceGenerationJobStatus) -> str:
    return value


def deserialize_json(data: str) -> AudienceGenerationJobStatus:
    if data not in _VALUES:
        raise DeserializationError(
            f"unknown AudienceGenerationJobStatus value: {data!r}"
        )
    return cast(AudienceGenerationJobStatus, data)
