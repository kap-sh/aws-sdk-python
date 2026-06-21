"""Generated from Smithy shape ``com.amazonaws.codeartifact#PackageVersionSortType``."""

from typing import Literal, TypeAlias, cast

PackageVersionSortType: TypeAlias = Literal["PUBLISHED_TIME",]


# --- restJson1 ser/de ---
def serialize_json(value: PackageVersionSortType) -> str:
    return value


def deserialize_json(data: str) -> PackageVersionSortType:
    return cast(PackageVersionSortType, data)
