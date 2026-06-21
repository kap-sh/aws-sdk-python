"""Generated from Smithy shape ``com.amazonaws.medialive#GlobalConfigurationInputEndAction``."""

from typing import Literal, TypeAlias, cast

"""Global Configuration Input End Action"""
GlobalConfigurationInputEndAction: TypeAlias = Literal[
    "NONE",
    "SWITCH_AND_LOOP_INPUTS",
]


# --- restJson1 ser/de ---
def serialize_json(value: GlobalConfigurationInputEndAction) -> str:
    return value


def deserialize_json(data: str) -> GlobalConfigurationInputEndAction:
    return cast(GlobalConfigurationInputEndAction, data)
