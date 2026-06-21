"""Generated from Smithy shape ``com.amazonaws.opensearch#ZoneStatus``."""

from typing import Literal, TypeAlias, cast

ZoneStatus: TypeAlias = Literal[
    "Active",
    "StandBy",
    "NotAvailable",
]


# --- restJson1 ser/de ---
def serialize_json(value: ZoneStatus) -> str:
    return value


def deserialize_json(data: str) -> ZoneStatus:
    return cast(ZoneStatus, data)
