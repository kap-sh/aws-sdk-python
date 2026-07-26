"""Generated from Smithy shape ``com.amazonaws.iot#PackageVersionAction``."""

from typing import Literal, TypeAlias, cast

PackageVersionAction: TypeAlias = Literal[
    "PUBLISH",
    "DEPRECATE",
]


# --- restJson1 ser/de ---
def serialize_json(value: PackageVersionAction) -> str:
    return value


def deserialize_json(data: str) -> PackageVersionAction:
    return cast(PackageVersionAction, data)
