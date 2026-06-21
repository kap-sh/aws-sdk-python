"""Generated from Smithy shape ``com.amazonaws.greengrass#SoftwareToUpdate``."""

from typing import Literal, TypeAlias, cast

"""The piece of software on the Greengrass core that will be updated."""
SoftwareToUpdate: TypeAlias = Literal[
    "core",
    "ota_agent",
]


# --- restJson1 ser/de ---
def serialize_json(value: SoftwareToUpdate) -> str:
    return value


def deserialize_json(data: str) -> SoftwareToUpdate:
    return cast(SoftwareToUpdate, data)
