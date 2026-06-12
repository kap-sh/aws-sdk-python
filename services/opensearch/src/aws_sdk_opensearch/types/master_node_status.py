"""Generated from Smithy shape ``com.amazonaws.opensearch#MasterNodeStatus``."""

from typing import Literal, TypeAlias, cast

from aws_sdk_opensearch.errors import DeserializationError

MasterNodeStatus: TypeAlias = Literal[
    "Available",
    "UnAvailable",
]


# --- restJson1 ser/de ---
_VALUES: frozenset[str] = frozenset(
    (
        "Available",
        "UnAvailable",
    )
)


def serialize_json(value: MasterNodeStatus) -> str:
    return value


def deserialize_json(data: str) -> MasterNodeStatus:
    if data not in _VALUES:
        raise DeserializationError(f"unknown MasterNodeStatus value: {data!r}")
    return cast(MasterNodeStatus, data)
