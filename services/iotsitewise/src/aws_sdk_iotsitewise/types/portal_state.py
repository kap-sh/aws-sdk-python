"""Generated from Smithy shape ``com.amazonaws.iotsitewise#PortalState``."""

from typing import Literal, TypeAlias, cast

from aws_sdk_iotsitewise.errors import DeserializationError

PortalState: TypeAlias = Literal[
    "CREATING",
    "PENDING",
    "UPDATING",
    "DELETING",
    "ACTIVE",
    "FAILED",
]


# --- restJson1 ser/de ---
_VALUES: frozenset[str] = frozenset(
    (
        "CREATING",
        "PENDING",
        "UPDATING",
        "DELETING",
        "ACTIVE",
        "FAILED",
    )
)


def serialize_json(value: PortalState) -> str:
    return value


def deserialize_json(data: str) -> PortalState:
    if data not in _VALUES:
        raise DeserializationError(f"unknown PortalState value: {data!r}")
    return cast(PortalState, data)
