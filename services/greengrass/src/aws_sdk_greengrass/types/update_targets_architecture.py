"""Generated from Smithy shape ``com.amazonaws.greengrass#UpdateTargetsArchitecture``."""

from typing import Literal, TypeAlias, cast

from aws_sdk_greengrass.errors import DeserializationError

"""The architecture of the cores which are the targets of an update."""
UpdateTargetsArchitecture: TypeAlias = Literal[
    "armv6l",
    "armv7l",
    "x86_64",
    "aarch64",
]


# --- restJson1 ser/de ---
_VALUES: frozenset[str] = frozenset(
    (
        "armv6l",
        "armv7l",
        "x86_64",
        "aarch64",
    )
)


def serialize_json(value: UpdateTargetsArchitecture) -> str:
    return value


def deserialize_json(data: str) -> UpdateTargetsArchitecture:
    if data not in _VALUES:
        raise DeserializationError(f"unknown UpdateTargetsArchitecture value: {data!r}")
    return cast(UpdateTargetsArchitecture, data)
