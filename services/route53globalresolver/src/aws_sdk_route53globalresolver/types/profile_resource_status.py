"""Generated from Smithy shape ``com.amazonaws.route53globalresolver#ProfileResourceStatus``."""

from typing import Literal, TypeAlias, cast

from aws_sdk_route53globalresolver.errors import DeserializationError

ProfileResourceStatus: TypeAlias = Literal[
    "CREATING",
    "OPERATIONAL",
    "UPDATING",
    "ENABLING",
    "DISABLING",
    "DISABLED",
    "DELETING",
]


# --- restJson1 ser/de ---
_VALUES: frozenset[str] = frozenset(
    (
        "CREATING",
        "OPERATIONAL",
        "UPDATING",
        "ENABLING",
        "DISABLING",
        "DISABLED",
        "DELETING",
    )
)


def serialize_json(value: ProfileResourceStatus) -> str:
    return value


def deserialize_json(data: str) -> ProfileResourceStatus:
    if data not in _VALUES:
        raise DeserializationError(f"unknown ProfileResourceStatus value: {data!r}")
    return cast(ProfileResourceStatus, data)
