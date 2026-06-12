"""Generated from Smithy shape ``com.amazonaws.greengrass#SoftwareToUpdate``."""

from typing import Literal, TypeAlias, cast

from aws_sdk_greengrass.errors import DeserializationError

"""The piece of software on the Greengrass core that will be updated."""
SoftwareToUpdate: TypeAlias = Literal[
    "core",
    "ota_agent",
]


# --- restJson1 ser/de ---
_VALUES: frozenset[str] = frozenset(
    (
        "core",
        "ota_agent",
    )
)


def serialize_json(value: SoftwareToUpdate) -> str:
    return value


def deserialize_json(data: str) -> SoftwareToUpdate:
    if data not in _VALUES:
        raise DeserializationError(f"unknown SoftwareToUpdate value: {data!r}")
    return cast(SoftwareToUpdate, data)
