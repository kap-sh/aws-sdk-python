"""Generated from Smithy shape ``com.amazonaws.guardduty#ManagementType``."""

from typing import Literal, TypeAlias, cast

ManagementType: TypeAlias = Literal[
    "AUTO_MANAGED",
    "MANUAL",
    "DISABLED",
]


# --- restJson1 ser/de ---
def serialize_json(value: ManagementType) -> str:
    return value


def deserialize_json(data: str) -> ManagementType:
    return cast(ManagementType, data)
