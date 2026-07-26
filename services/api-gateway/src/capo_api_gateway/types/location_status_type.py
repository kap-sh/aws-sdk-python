"""Generated from Smithy shape ``com.amazonaws.apigateway#LocationStatusType``."""

from typing import Literal, TypeAlias, cast

LocationStatusType: TypeAlias = Literal[
    "DOCUMENTED",
    "UNDOCUMENTED",
]


# --- restJson1 ser/de ---
def serialize_json(value: LocationStatusType) -> str:
    return value


def deserialize_json(data: str) -> LocationStatusType:
    return cast(LocationStatusType, data)
