"""Generated from Smithy shape ``com.amazonaws.ssmsap#ConfigurationCheckType``."""

from typing import Literal, TypeAlias, cast

ConfigurationCheckType: TypeAlias = Literal[
    "SAP_CHECK_01",
    "SAP_CHECK_02",
    "SAP_CHECK_03",
]


# --- restJson1 ser/de ---
def serialize_json(value: ConfigurationCheckType) -> str:
    return value


def deserialize_json(data: str) -> ConfigurationCheckType:
    return cast(ConfigurationCheckType, data)
