"""Generated from Smithy shape ``com.amazonaws.greengrass#UpdateTargetsOperatingSystem``."""

from typing import Literal, TypeAlias, cast

"""The operating system of the cores which are the targets of an update."""
UpdateTargetsOperatingSystem: TypeAlias = Literal[
    "ubuntu",
    "raspbian",
    "amazon_linux",
    "openwrt",
]


# --- restJson1 ser/de ---
def serialize_json(value: UpdateTargetsOperatingSystem) -> str:
    return value


def deserialize_json(data: str) -> UpdateTargetsOperatingSystem:
    return cast(UpdateTargetsOperatingSystem, data)
