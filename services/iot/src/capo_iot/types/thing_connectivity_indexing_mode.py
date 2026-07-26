"""Generated from Smithy shape ``com.amazonaws.iot#ThingConnectivityIndexingMode``."""

from typing import Literal, TypeAlias, cast

ThingConnectivityIndexingMode: TypeAlias = Literal[
    "OFF",
    "STATUS",
]


# --- restJson1 ser/de ---
def serialize_json(value: ThingConnectivityIndexingMode) -> str:
    return value


def deserialize_json(data: str) -> ThingConnectivityIndexingMode:
    return cast(ThingConnectivityIndexingMode, data)
