"""Generated from Smithy shape ``com.amazonaws.opensearch#UpgradeStatus``."""

from typing import Literal, TypeAlias, cast

UpgradeStatus: TypeAlias = Literal[
    "IN_PROGRESS",
    "SUCCEEDED",
    "SUCCEEDED_WITH_ISSUES",
    "FAILED",
]


# --- restJson1 ser/de ---
def serialize_json(value: UpgradeStatus) -> str:
    return value


def deserialize_json(data: str) -> UpgradeStatus:
    return cast(UpgradeStatus, data)
