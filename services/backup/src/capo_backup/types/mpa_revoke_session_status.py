"""Generated from Smithy shape ``com.amazonaws.backup#MpaRevokeSessionStatus``."""

from typing import Literal, TypeAlias, cast

MpaRevokeSessionStatus: TypeAlias = Literal[
    "PENDING",
    "FAILED",
]


# --- restJson1 ser/de ---
def serialize_json(value: MpaRevokeSessionStatus) -> str:
    return value


def deserialize_json(data: str) -> MpaRevokeSessionStatus:
    return cast(MpaRevokeSessionStatus, data)
