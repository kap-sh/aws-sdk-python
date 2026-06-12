"""Generated from Smithy shape ``com.amazonaws.ebs#ResourceNotFoundExceptionReason``."""

from typing import Literal, TypeAlias, cast

from aws_sdk_ebs.errors import DeserializationError

ResourceNotFoundExceptionReason: TypeAlias = Literal[
    "SNAPSHOT_NOT_FOUND",
    "GRANT_NOT_FOUND",
    "DEPENDENCY_RESOURCE_NOT_FOUND",
    "IMAGE_NOT_FOUND",
]


# --- restJson1 ser/de ---
_VALUES: frozenset[str] = frozenset(
    (
        "SNAPSHOT_NOT_FOUND",
        "GRANT_NOT_FOUND",
        "DEPENDENCY_RESOURCE_NOT_FOUND",
        "IMAGE_NOT_FOUND",
    )
)


def serialize_json(value: ResourceNotFoundExceptionReason) -> str:
    return value


def deserialize_json(data: str) -> ResourceNotFoundExceptionReason:
    if data not in _VALUES:
        raise DeserializationError(
            f"unknown ResourceNotFoundExceptionReason value: {data!r}"
        )
    return cast(ResourceNotFoundExceptionReason, data)
