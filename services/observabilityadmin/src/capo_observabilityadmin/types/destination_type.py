"""Generated from Smithy shape ``com.amazonaws.observabilityadmin#DestinationType``."""

from typing import Literal, TypeAlias, cast

DestinationType: TypeAlias = Literal["cloud-watch-logs",]


# --- restJson1 ser/de ---
def serialize_json(value: DestinationType) -> str:
    return value


def deserialize_json(data: str) -> DestinationType:
    return cast(DestinationType, data)
