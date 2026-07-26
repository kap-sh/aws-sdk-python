"""Generated from Smithy shape ``com.amazonaws.elasticsearchservice#PackageType``."""

from typing import Literal, TypeAlias, cast

PackageType: TypeAlias = Literal["TXT-DICTIONARY",]


# --- restJson1 ser/de ---
def serialize_json(value: PackageType) -> str:
    return value


def deserialize_json(data: str) -> PackageType:
    return cast(PackageType, data)
