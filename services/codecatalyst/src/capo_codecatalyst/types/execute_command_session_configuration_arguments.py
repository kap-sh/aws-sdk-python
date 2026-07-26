"""Generated from Smithy shape ``com.amazonaws.codecatalyst#ExecuteCommandSessionConfigurationArguments``."""

from typing import TypeAlias

ExecuteCommandSessionConfigurationArguments: TypeAlias = list["str"]


# --- restJson1 ser/de ---
def serialize_json(value: ExecuteCommandSessionConfigurationArguments) -> list:
    return list(value)


def deserialize_json(data: list) -> ExecuteCommandSessionConfigurationArguments:
    return list(data)
