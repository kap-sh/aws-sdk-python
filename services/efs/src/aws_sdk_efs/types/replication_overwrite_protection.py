"""Generated from Smithy shape ``com.amazonaws.efs#ReplicationOverwriteProtection``."""

from typing import Literal, TypeAlias, cast

from aws_sdk_efs.errors import DeserializationError

ReplicationOverwriteProtection: TypeAlias = Literal[
    "ENABLED",
    "DISABLED",
    "REPLICATING",
]


# --- restJson1 ser/de ---
_VALUES: frozenset[str] = frozenset(
    (
        "ENABLED",
        "DISABLED",
        "REPLICATING",
    )
)


def serialize_json(value: ReplicationOverwriteProtection) -> str:
    return value


def deserialize_json(data: str) -> ReplicationOverwriteProtection:
    if data not in _VALUES:
        raise DeserializationError(
            f"unknown ReplicationOverwriteProtection value: {data!r}"
        )
    return cast(ReplicationOverwriteProtection, data)
