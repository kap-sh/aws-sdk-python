"""Generated from Smithy shape ``com.amazonaws.quicksight#SelfUpgradeAdminAction``."""

from typing import Literal, TypeAlias, cast

SelfUpgradeAdminAction: TypeAlias = Literal[
    "APPROVE",
    "DENY",
    "VERIFY",
]


# --- restJson1 ser/de ---
def serialize_json(value: SelfUpgradeAdminAction) -> str:
    return value


def deserialize_json(data: str) -> SelfUpgradeAdminAction:
    return cast(SelfUpgradeAdminAction, data)
