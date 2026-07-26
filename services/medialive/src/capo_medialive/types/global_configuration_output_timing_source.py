"""Generated from Smithy shape ``com.amazonaws.medialive#GlobalConfigurationOutputTimingSource``."""

from typing import Literal, TypeAlias, cast

"""Global Configuration Output Timing Source"""
GlobalConfigurationOutputTimingSource: TypeAlias = Literal[
    "INPUT_CLOCK",
    "SYSTEM_CLOCK",
]


# --- restJson1 ser/de ---
def serialize_json(value: GlobalConfigurationOutputTimingSource) -> str:
    return value


def deserialize_json(data: str) -> GlobalConfigurationOutputTimingSource:
    return cast(GlobalConfigurationOutputTimingSource, data)
