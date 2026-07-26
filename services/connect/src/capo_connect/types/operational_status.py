"""Generated from Smithy shape ``com.amazonaws.connect#OperationalStatus``."""

from typing import Literal, TypeAlias, cast

OperationalStatus: TypeAlias = Literal[
    "OPEN",
    "CLOSED",
]


# --- restJson1 ser/de ---
def serialize_json(value: OperationalStatus) -> str:
    return value


def deserialize_json(data: str) -> OperationalStatus:
    return cast(OperationalStatus, data)
