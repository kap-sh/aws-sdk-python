"""Generated from Smithy shape ``com.amazonaws.iotwireless#DlClass``."""

from typing import Literal, TypeAlias, cast

"""<p>DlClass for LoRaWAM, valid values are ClassB and ClassC.</p>"""
DlClass: TypeAlias = Literal[
    "ClassB",
    "ClassC",
]


# --- restJson1 ser/de ---
def serialize_json(value: DlClass) -> str:
    return value


def deserialize_json(data: str) -> DlClass:
    return cast(DlClass, data)
