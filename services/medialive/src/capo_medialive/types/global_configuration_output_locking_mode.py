"""Generated from Smithy shape ``com.amazonaws.medialive#GlobalConfigurationOutputLockingMode``."""

from typing import Literal, TypeAlias, cast

"""Global Configuration Output Locking Mode"""
GlobalConfigurationOutputLockingMode: TypeAlias = Literal[
    "EPOCH_LOCKING",
    "PIPELINE_LOCKING",
    "DISABLED",
]


# --- restJson1 ser/de ---
def serialize_json(value: GlobalConfigurationOutputLockingMode) -> str:
    return value


def deserialize_json(data: str) -> GlobalConfigurationOutputLockingMode:
    return cast(GlobalConfigurationOutputLockingMode, data)
