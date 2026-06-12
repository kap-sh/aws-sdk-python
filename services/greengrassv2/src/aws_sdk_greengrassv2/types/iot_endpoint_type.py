"""Generated from Smithy shape ``com.amazonaws.greengrassv2#IotEndpointType``."""

from typing import Literal, TypeAlias, cast

from aws_sdk_greengrassv2.errors import DeserializationError

IotEndpointType: TypeAlias = Literal[
    "fips",
    "standard",
]


# --- restJson1 ser/de ---
_VALUES: frozenset[str] = frozenset(
    (
        "fips",
        "standard",
    )
)


def serialize_json(value: IotEndpointType) -> str:
    return value


def deserialize_json(data: str) -> IotEndpointType:
    if data not in _VALUES:
        raise DeserializationError(f"unknown IotEndpointType value: {data!r}")
    return cast(IotEndpointType, data)
