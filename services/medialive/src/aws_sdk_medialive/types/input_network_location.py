"""Generated from Smithy shape ``com.amazonaws.medialive#InputNetworkLocation``."""

from typing import Literal, TypeAlias, cast

from aws_sdk_medialive.errors import DeserializationError

"""With the introduction of MediaLive Anywhere, a MediaLive input can now exist in two different places: AWS or inside an on-premises datacenter. By default all inputs will continue to be AWS inputs."""
InputNetworkLocation: TypeAlias = Literal[
    "AWS",
    "ON_PREMISES",
]


# --- restJson1 ser/de ---
_VALUES: frozenset[str] = frozenset(
    (
        "AWS",
        "ON_PREMISES",
    )
)


def serialize_json(value: InputNetworkLocation) -> str:
    return value


def deserialize_json(data: str) -> InputNetworkLocation:
    if data not in _VALUES:
        raise DeserializationError(f"unknown InputNetworkLocation value: {data!r}")
    return cast(InputNetworkLocation, data)
