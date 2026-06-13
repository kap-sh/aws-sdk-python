"""Generated from Smithy shape ``com.amazonaws.quicksight#SelfUpgradeAdminAction``."""

from typing import Literal, TypeAlias, cast

from aws_sdk_quicksight.errors import DeserializationError

SelfUpgradeAdminAction: TypeAlias = Literal[
    "APPROVE",
    "DENY",
    "VERIFY",
]


# --- restJson1 ser/de ---
_VALUES: frozenset[str] = frozenset(
    (
        "APPROVE",
        "DENY",
        "VERIFY",
    )
)


def serialize_json(value: SelfUpgradeAdminAction) -> str:
    return value


def deserialize_json(data: str) -> SelfUpgradeAdminAction:
    if data not in _VALUES:
        raise DeserializationError(f"unknown SelfUpgradeAdminAction value: {data!r}")
    return cast(SelfUpgradeAdminAction, data)
