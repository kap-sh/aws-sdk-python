"""Generated from Smithy shape ``com.amazonaws.s3outposts#EndpointStatus``."""

from typing import Literal, TypeAlias, cast

from aws_sdk_s3outposts.errors import DeserializationError

EndpointStatus: TypeAlias = Literal[
    "Pending",
    "Available",
    "Deleting",
    "Create_Failed",
    "Delete_Failed",
]


# --- restJson1 ser/de ---
_VALUES: frozenset[str] = frozenset(
    (
        "Pending",
        "Available",
        "Deleting",
        "Create_Failed",
        "Delete_Failed",
    )
)


def serialize_json(value: EndpointStatus) -> str:
    return value


def deserialize_json(data: str) -> EndpointStatus:
    if data not in _VALUES:
        raise DeserializationError(f"unknown EndpointStatus value: {data!r}")
    return cast(EndpointStatus, data)
