"""Generated from Smithy shape ``com.amazonaws.efs#Resource``."""

from typing import Literal, TypeAlias, cast

"""An EFS resource, for example a file system or a mount target."""
Resource: TypeAlias = Literal[
    "FILE_SYSTEM",
    "MOUNT_TARGET",
]


# --- restJson1 ser/de ---
def serialize_json(value: Resource) -> str:
    return value


def deserialize_json(data: str) -> Resource:
    return cast(Resource, data)
