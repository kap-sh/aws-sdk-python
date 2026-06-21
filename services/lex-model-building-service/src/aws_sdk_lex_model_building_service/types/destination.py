"""Generated from Smithy shape ``com.amazonaws.lexmodelbuildingservice#Destination``."""

from typing import Literal, TypeAlias, cast

Destination: TypeAlias = Literal[
    "CLOUDWATCH_LOGS",
    "S3",
]


# --- restJson1 ser/de ---
def serialize_json(value: Destination) -> str:
    return value


def deserialize_json(data: str) -> Destination:
    return cast(Destination, data)
