"""Generated from Smithy shape ``com.amazonaws.medialive#GlobalConfigurationLowFramerateInputs``."""

from typing import Literal, TypeAlias, cast

"""Global Configuration Low Framerate Inputs"""
GlobalConfigurationLowFramerateInputs: TypeAlias = Literal[
    "DISABLED",
    "ENABLED",
]


# --- restJson1 ser/de ---
def serialize_json(value: GlobalConfigurationLowFramerateInputs) -> str:
    return value


def deserialize_json(data: str) -> GlobalConfigurationLowFramerateInputs:
    return cast(GlobalConfigurationLowFramerateInputs, data)
