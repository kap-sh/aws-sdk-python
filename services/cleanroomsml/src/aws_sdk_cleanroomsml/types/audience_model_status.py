"""Generated from Smithy shape ``com.amazonaws.cleanroomsml#AudienceModelStatus``."""

from typing import Literal, TypeAlias, cast

from aws_sdk_cleanroomsml.errors import DeserializationError

AudienceModelStatus: TypeAlias = Literal[
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


def serialize_json(value: AudienceModelStatus) -> str:
    return value


def deserialize_json(data: str) -> AudienceModelStatus:
    if data not in _VALUES:
        raise DeserializationError(f"unknown AudienceModelStatus value: {data!r}")
    return cast(AudienceModelStatus, data)
