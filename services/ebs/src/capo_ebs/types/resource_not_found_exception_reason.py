"""Generated from Smithy shape ``com.amazonaws.ebs#ResourceNotFoundExceptionReason``."""

from typing import Literal, TypeAlias, cast

ResourceNotFoundExceptionReason: TypeAlias = Literal[
    "SNAPSHOT_NOT_FOUND",
    "GRANT_NOT_FOUND",
    "DEPENDENCY_RESOURCE_NOT_FOUND",
    "IMAGE_NOT_FOUND",
]


# --- restJson1 ser/de ---
def serialize_json(value: ResourceNotFoundExceptionReason) -> str:
    return value


def deserialize_json(data: str) -> ResourceNotFoundExceptionReason:
    return cast(ResourceNotFoundExceptionReason, data)
