"""Generated from Smithy shape ``com.amazonaws.quicksight#SpaceQuickSightResourceType``."""

from typing import Literal, TypeAlias, cast

from aws_sdk_quicksight.errors import DeserializationError

SpaceQuickSightResourceType: TypeAlias = Literal[
    "TOPIC",
    "DASHBOARD",
    "KNOWLEDGE_BASE",
    "SPACE",
    "ACTION_CONNECTOR",
    "DATA_SET",
    "ARTIFACT",
]


# --- restJson1 ser/de ---
_VALUES: frozenset[str] = frozenset(
    (
        "TOPIC",
        "DASHBOARD",
        "KNOWLEDGE_BASE",
        "SPACE",
        "ACTION_CONNECTOR",
        "DATA_SET",
        "ARTIFACT",
    )
)


def serialize_json(value: SpaceQuickSightResourceType) -> str:
    return value


def deserialize_json(data: str) -> SpaceQuickSightResourceType:
    if data not in _VALUES:
        raise DeserializationError(
            f"unknown SpaceQuickSightResourceType value: {data!r}"
        )
    return cast(SpaceQuickSightResourceType, data)
