"""Generated from Smithy shape ``com.amazonaws.opensearch#PackageType``."""

from typing import Literal, TypeAlias, cast

PackageType: TypeAlias = Literal[
    "TXT-DICTIONARY",
    "ZIP-PLUGIN",
    "PACKAGE-LICENSE",
    "PACKAGE-CONFIG",
]


# --- restJson1 ser/de ---
def serialize_json(value: PackageType) -> str:
    return value


def deserialize_json(data: str) -> PackageType:
    return cast(PackageType, data)
