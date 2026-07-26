"""Generated from Smithy shape ``com.amazonaws.codeartifact#PackageVersionOriginType``."""

from typing import Literal, TypeAlias, cast

PackageVersionOriginType: TypeAlias = Literal[
    "INTERNAL",
    "EXTERNAL",
    "UNKNOWN",
]


# --- restJson1 ser/de ---
def serialize_json(value: PackageVersionOriginType) -> str:
    return value


def deserialize_json(data: str) -> PackageVersionOriginType:
    return cast(PackageVersionOriginType, data)
