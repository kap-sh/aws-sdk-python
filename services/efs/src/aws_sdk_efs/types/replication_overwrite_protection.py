"""Generated from Smithy shape ``com.amazonaws.efs#ReplicationOverwriteProtection``."""

from typing import Literal, TypeAlias, cast

ReplicationOverwriteProtection: TypeAlias = Literal[
    "ENABLED",
    "DISABLED",
    "REPLICATING",
]


# --- restJson1 ser/de ---
def serialize_json(value: ReplicationOverwriteProtection) -> str:
    return value


def deserialize_json(data: str) -> ReplicationOverwriteProtection:
    return cast(ReplicationOverwriteProtection, data)
