"""Generated from Smithy shape ``com.amazonaws.resiliencehub#HaArchitecture``."""

from typing import Literal, TypeAlias, cast

HaArchitecture: TypeAlias = Literal[
    "MultiSite",
    "WarmStandby",
    "PilotLight",
    "BackupAndRestore",
    "NoRecoveryPlan",
]


# --- restJson1 ser/de ---
def serialize_json(value: HaArchitecture) -> str:
    return value


def deserialize_json(data: str) -> HaArchitecture:
    return cast(HaArchitecture, data)
