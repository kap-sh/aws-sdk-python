"""Generated from Smithy shape ``com.amazonaws.eks#RepairAction``."""

from typing import Literal, TypeAlias, cast

RepairAction: TypeAlias = Literal[
    "Replace",
    "Reboot",
    "NoAction",
]


# --- restJson1 ser/de ---
def serialize_json(value: RepairAction) -> str:
    return value


def deserialize_json(data: str) -> RepairAction:
    return cast(RepairAction, data)
