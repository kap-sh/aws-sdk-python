"""Generated from Smithy shape ``com.amazonaws.greengrass#UpdateTargetsOperatingSystem``."""

from typing import Literal, TypeAlias, cast

from aws_sdk_greengrass.errors import DeserializationError

"""The operating system of the cores which are the targets of an update."""
UpdateTargetsOperatingSystem: TypeAlias = Literal[
    "ubuntu",
    "raspbian",
    "amazon_linux",
    "openwrt",
]


# --- restJson1 ser/de ---
_VALUES: frozenset[str] = frozenset(
    (
        "ubuntu",
        "raspbian",
        "amazon_linux",
        "openwrt",
    )
)


def serialize_json(value: UpdateTargetsOperatingSystem) -> str:
    return value


def deserialize_json(data: str) -> UpdateTargetsOperatingSystem:
    if data not in _VALUES:
        raise DeserializationError(
            f"unknown UpdateTargetsOperatingSystem value: {data!r}"
        )
    return cast(UpdateTargetsOperatingSystem, data)
