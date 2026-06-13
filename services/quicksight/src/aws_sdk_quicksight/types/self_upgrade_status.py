"""Generated from Smithy shape ``com.amazonaws.quicksight#SelfUpgradeStatus``."""

from typing import Literal, TypeAlias, cast

from aws_sdk_quicksight.errors import DeserializationError

SelfUpgradeStatus: TypeAlias = Literal[
    "AUTO_APPROVAL",
    "ADMIN_APPROVAL",
]


# --- restJson1 ser/de ---
_VALUES: frozenset[str] = frozenset(
    (
        "AUTO_APPROVAL",
        "ADMIN_APPROVAL",
    )
)


def serialize_json(value: SelfUpgradeStatus) -> str:
    return value


def deserialize_json(data: str) -> SelfUpgradeStatus:
    if data not in _VALUES:
        raise DeserializationError(f"unknown SelfUpgradeStatus value: {data!r}")
    return cast(SelfUpgradeStatus, data)
