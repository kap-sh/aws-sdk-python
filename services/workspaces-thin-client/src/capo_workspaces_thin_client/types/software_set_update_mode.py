"""Generated from Smithy shape ``com.amazonaws.workspacesthinclient#SoftwareSetUpdateMode``."""

from typing import Literal, TypeAlias, cast

SoftwareSetUpdateMode: TypeAlias = Literal[
    "USE_LATEST",
    "USE_DESIRED",
]


# --- restJson1 ser/de ---
def serialize_json(value: SoftwareSetUpdateMode) -> str:
    return value


def deserialize_json(data: str) -> SoftwareSetUpdateMode:
    return cast(SoftwareSetUpdateMode, data)
