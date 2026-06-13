"""Generated from Smithy shape ``com.amazonaws.qbusiness#WebExperienceStatus``."""

from typing import Literal, TypeAlias, cast

from aws_sdk_qbusiness.errors import DeserializationError

WebExperienceStatus: TypeAlias = Literal[
    "CREATING",
    "ACTIVE",
    "DELETING",
    "FAILED",
    "PENDING_AUTH_CONFIG",
]


# --- restJson1 ser/de ---
_VALUES: frozenset[str] = frozenset(
    (
        "CREATING",
        "ACTIVE",
        "DELETING",
        "FAILED",
        "PENDING_AUTH_CONFIG",
    )
)


def serialize_json(value: WebExperienceStatus) -> str:
    return value


def deserialize_json(data: str) -> WebExperienceStatus:
    if data not in _VALUES:
        raise DeserializationError(f"unknown WebExperienceStatus value: {data!r}")
    return cast(WebExperienceStatus, data)
