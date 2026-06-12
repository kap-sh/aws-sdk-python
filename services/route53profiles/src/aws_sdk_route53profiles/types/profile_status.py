"""Generated from Smithy shape ``com.amazonaws.route53profiles#ProfileStatus``."""

from typing import Literal, TypeAlias, cast

from aws_sdk_route53profiles.errors import DeserializationError

ProfileStatus: TypeAlias = Literal[
    "COMPLETE",
    "DELETING",
    "UPDATING",
    "CREATING",
    "DELETED",
    "FAILED",
]


# --- restJson1 ser/de ---
_VALUES: frozenset[str] = frozenset(
    (
        "COMPLETE",
        "DELETING",
        "UPDATING",
        "CREATING",
        "DELETED",
        "FAILED",
    )
)


def serialize_json(value: ProfileStatus) -> str:
    return value


def deserialize_json(data: str) -> ProfileStatus:
    if data not in _VALUES:
        raise DeserializationError(f"unknown ProfileStatus value: {data!r}")
    return cast(ProfileStatus, data)
