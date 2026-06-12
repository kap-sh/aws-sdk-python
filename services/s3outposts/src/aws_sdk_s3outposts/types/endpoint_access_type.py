"""Generated from Smithy shape ``com.amazonaws.s3outposts#EndpointAccessType``."""

from typing import Literal, TypeAlias, cast

from aws_sdk_s3outposts.errors import DeserializationError

EndpointAccessType: TypeAlias = Literal[
    "Private",
    "CustomerOwnedIp",
]


# --- restJson1 ser/de ---
_VALUES: frozenset[str] = frozenset(
    (
        "Private",
        "CustomerOwnedIp",
    )
)


def serialize_json(value: EndpointAccessType) -> str:
    return value


def deserialize_json(data: str) -> EndpointAccessType:
    if data not in _VALUES:
        raise DeserializationError(f"unknown EndpointAccessType value: {data!r}")
    return cast(EndpointAccessType, data)
