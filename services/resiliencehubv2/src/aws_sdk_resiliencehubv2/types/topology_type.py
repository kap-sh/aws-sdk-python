"""Generated from Smithy shape ``com.amazonaws.resiliencehubv2#TopologyType``."""

from typing import Literal, TypeAlias, cast

from aws_sdk_resiliencehubv2.errors import DeserializationError

TopologyType: TypeAlias = Literal[
    "CONTAINMENT",
    "DATA_FLOW",
    "OBSERVABILITY",
    "PERMISSIONS",
]


# --- restJson1 ser/de ---
_VALUES: frozenset[str] = frozenset(
    (
        "CONTAINMENT",
        "DATA_FLOW",
        "OBSERVABILITY",
        "PERMISSIONS",
    )
)


def serialize_json(value: TopologyType) -> str:
    return value


def deserialize_json(data: str) -> TopologyType:
    if data not in _VALUES:
        raise DeserializationError(f"unknown TopologyType value: {data!r}")
    return cast(TopologyType, data)
