"""Generated from Smithy shape ``com.amazonaws.taxsettings#HeritageStatus``."""

from typing import Literal, TypeAlias, cast

HeritageStatus: TypeAlias = Literal[
    "OptIn",
    "OptOut",
]


# --- restJson1 ser/de ---
def serialize_json(value: HeritageStatus) -> str:
    return value


def deserialize_json(data: str) -> HeritageStatus:
    return cast(HeritageStatus, data)
