"""Generated from Smithy shape ``com.amazonaws.eks#VersionStatus``."""

from typing import Literal, TypeAlias, cast

VersionStatus: TypeAlias = Literal[
    "UNSUPPORTED",
    "STANDARD_SUPPORT",
    "EXTENDED_SUPPORT",
]


# --- restJson1 ser/de ---
def serialize_json(value: VersionStatus) -> str:
    return value


def deserialize_json(data: str) -> VersionStatus:
    return cast(VersionStatus, data)
