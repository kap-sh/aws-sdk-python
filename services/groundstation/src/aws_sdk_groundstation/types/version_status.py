"""Generated from Smithy shape ``com.amazonaws.groundstation#VersionStatus``."""

from typing import Literal, TypeAlias, cast

VersionStatus: TypeAlias = Literal[
    "UPDATING",
    "ACTIVE",
    "SUPERSEDED",
    "FAILED_TO_UPDATE",
]


# --- restJson1 ser/de ---
def serialize_json(value: VersionStatus) -> str:
    return value


def deserialize_json(data: str) -> VersionStatus:
    return cast(VersionStatus, data)
