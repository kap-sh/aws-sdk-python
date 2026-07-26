"""Generated from Smithy shape ``com.amazonaws.tnb#PackageContentType``."""

from typing import Literal, TypeAlias, cast

PackageContentType: TypeAlias = Literal["application/zip",]


# --- restJson1 ser/de ---
def serialize_json(value: PackageContentType) -> str:
    return value


def deserialize_json(data: str) -> PackageContentType:
    return cast(PackageContentType, data)
