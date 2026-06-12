"""Generated from Smithy shape ``com.amazonaws.greengrassv2#S3EndpointType``."""

from typing import Literal, TypeAlias, cast

from aws_sdk_greengrassv2.errors import DeserializationError

S3EndpointType: TypeAlias = Literal[
    "REGIONAL",
    "GLOBAL",
]


# --- restJson1 ser/de ---
_VALUES: frozenset[str] = frozenset(
    (
        "REGIONAL",
        "GLOBAL",
    )
)


def serialize_json(value: S3EndpointType) -> str:
    return value


def deserialize_json(data: str) -> S3EndpointType:
    if data not in _VALUES:
        raise DeserializationError(f"unknown S3EndpointType value: {data!r}")
    return cast(S3EndpointType, data)
