"""Generated from Smithy shape ``com.amazonaws.datazone#EnableSetting``."""

from typing import Literal, TypeAlias, cast

EnableSetting: TypeAlias = Literal[
    "ENABLED",
    "DISABLED",
]


# --- restJson1 ser/de ---
def serialize_json(value: EnableSetting) -> str:
    return value


def deserialize_json(data: str) -> EnableSetting:
    return cast(EnableSetting, data)
