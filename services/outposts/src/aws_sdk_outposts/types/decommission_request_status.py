"""Generated from Smithy shape ``com.amazonaws.outposts#DecommissionRequestStatus``."""

from typing import Literal, TypeAlias, cast

from aws_sdk_outposts.errors import DeserializationError

DecommissionRequestStatus: TypeAlias = Literal[
    "SKIPPED",
    "BLOCKED",
    "REQUESTED",
]


# --- restJson1 ser/de ---
_VALUES: frozenset[str] = frozenset(
    (
        "SKIPPED",
        "BLOCKED",
        "REQUESTED",
    )
)


def serialize_json(value: DecommissionRequestStatus) -> str:
    return value


def deserialize_json(data: str) -> DecommissionRequestStatus:
    if data not in _VALUES:
        raise DeserializationError(f"unknown DecommissionRequestStatus value: {data!r}")
    return cast(DecommissionRequestStatus, data)
