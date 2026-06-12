"""Generated from Smithy shape ``com.amazonaws.wellarchitected#ShareResourceType``."""

from typing import Literal, TypeAlias, cast

from aws_sdk_wellarchitected.errors import DeserializationError

ShareResourceType: TypeAlias = Literal[
    "WORKLOAD",
    "LENS",
    "PROFILE",
    "TEMPLATE",
]


# --- restJson1 ser/de ---
_VALUES: frozenset[str] = frozenset(
    (
        "WORKLOAD",
        "LENS",
        "PROFILE",
        "TEMPLATE",
    )
)


def serialize_json(value: ShareResourceType) -> str:
    return value


def deserialize_json(data: str) -> ShareResourceType:
    if data not in _VALUES:
        raise DeserializationError(f"unknown ShareResourceType value: {data!r}")
    return cast(ShareResourceType, data)
