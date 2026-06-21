"""Generated from Smithy shape ``com.amazonaws.greengrass#UpdateTargetsArchitecture``."""

from typing import Literal, TypeAlias, cast

"""The architecture of the cores which are the targets of an update."""
UpdateTargetsArchitecture: TypeAlias = Literal[
    "armv6l",
    "armv7l",
    "x86_64",
    "aarch64",
]


# --- restJson1 ser/de ---
def serialize_json(value: UpdateTargetsArchitecture) -> str:
    return value


def deserialize_json(data: str) -> UpdateTargetsArchitecture:
    return cast(UpdateTargetsArchitecture, data)
