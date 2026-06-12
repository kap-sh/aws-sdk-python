"""Generated from Smithy shape ``com.amazonaws.efs#Resource``."""

from typing import Literal, TypeAlias, cast

from aws_sdk_efs.errors import DeserializationError

"""An EFS resource, for example a file system or a mount target."""
Resource: TypeAlias = Literal[
    "FILE_SYSTEM",
    "MOUNT_TARGET",
]


# --- restJson1 ser/de ---
_VALUES: frozenset[str] = frozenset(
    (
        "FILE_SYSTEM",
        "MOUNT_TARGET",
    )
)


def serialize_json(value: Resource) -> str:
    return value


def deserialize_json(data: str) -> Resource:
    if data not in _VALUES:
        raise DeserializationError(f"unknown Resource value: {data!r}")
    return cast(Resource, data)
