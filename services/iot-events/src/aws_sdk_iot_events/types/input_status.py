"""Generated from Smithy shape ``com.amazonaws.iotevents#InputStatus``."""

from typing import Literal, TypeAlias, cast

InputStatus: TypeAlias = Literal[
    "CREATING",
    "UPDATING",
    "ACTIVE",
    "DELETING",
]


# --- restJson1 ser/de ---
def serialize_json(value: InputStatus) -> str:
    return value


def deserialize_json(data: str) -> InputStatus:
    return cast(InputStatus, data)
