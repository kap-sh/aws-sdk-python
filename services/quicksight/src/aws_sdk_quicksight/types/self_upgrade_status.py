"""Generated from Smithy shape ``com.amazonaws.quicksight#SelfUpgradeStatus``."""

from typing import Literal, TypeAlias, cast

SelfUpgradeStatus: TypeAlias = Literal[
    "AUTO_APPROVAL",
    "ADMIN_APPROVAL",
]


# --- restJson1 ser/de ---
def serialize_json(value: SelfUpgradeStatus) -> str:
    return value


def deserialize_json(data: str) -> SelfUpgradeStatus:
    return cast(SelfUpgradeStatus, data)
