"""Generated from Smithy shape ``com.amazonaws.gameliftstreams#RuntimeEnvironmentType``."""

from typing import Literal, TypeAlias, cast

RuntimeEnvironmentType: TypeAlias = Literal[
    "PROTON",
    "WINDOWS",
    "UBUNTU",
]


# --- restJson1 ser/de ---
def serialize_json(value: RuntimeEnvironmentType) -> str:
    return value


def deserialize_json(data: str) -> RuntimeEnvironmentType:
    return cast(RuntimeEnvironmentType, data)
