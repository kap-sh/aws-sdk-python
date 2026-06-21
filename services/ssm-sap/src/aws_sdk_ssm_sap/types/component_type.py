"""Generated from Smithy shape ``com.amazonaws.ssmsap#ComponentType``."""

from typing import Literal, TypeAlias, cast

ComponentType: TypeAlias = Literal[
    "HANA",
    "HANA_NODE",
    "ABAP",
    "ASCS",
    "DIALOG",
    "WEBDISP",
    "WD",
    "ERS",
]


# --- restJson1 ser/de ---
def serialize_json(value: ComponentType) -> str:
    return value


def deserialize_json(data: str) -> ComponentType:
    return cast(ComponentType, data)
