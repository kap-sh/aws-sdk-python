"""Generated from Smithy shape ``com.amazonaws.ssmsap#ApplicationType``."""

from typing import Literal, TypeAlias, cast

ApplicationType: TypeAlias = Literal[
    "HANA",
    "SAP_ABAP",
]


# --- restJson1 ser/de ---
def serialize_json(value: ApplicationType) -> str:
    return value


def deserialize_json(data: str) -> ApplicationType:
    return cast(ApplicationType, data)
