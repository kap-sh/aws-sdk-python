"""Generated from Smithy shape ``com.amazonaws.elasticsearchservice#UpgradeStep``."""

from typing import Literal, TypeAlias, cast

UpgradeStep: TypeAlias = Literal[
    "PRE_UPGRADE_CHECK",
    "SNAPSHOT",
    "UPGRADE",
]


# --- restJson1 ser/de ---
def serialize_json(value: UpgradeStep) -> str:
    return value


def deserialize_json(data: str) -> UpgradeStep:
    return cast(UpgradeStep, data)
