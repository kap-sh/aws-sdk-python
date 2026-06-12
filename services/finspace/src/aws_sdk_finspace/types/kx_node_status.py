"""Generated from Smithy shape ``com.amazonaws.finspace#KxNodeStatus``."""

from typing import Literal, TypeAlias, cast

from aws_sdk_finspace.errors import DeserializationError

KxNodeStatus: TypeAlias = Literal[
    "RUNNING",
    "PROVISIONING",
]


# --- restJson1 ser/de ---
_VALUES: frozenset[str] = frozenset(
    (
        "RUNNING",
        "PROVISIONING",
    )
)


def serialize_json(value: KxNodeStatus) -> str:
    return value


def deserialize_json(data: str) -> KxNodeStatus:
    if data not in _VALUES:
        raise DeserializationError(f"unknown KxNodeStatus value: {data!r}")
    return cast(KxNodeStatus, data)
