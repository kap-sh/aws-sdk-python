"""Generated from Smithy shape ``com.amazonaws.ssmsap#ConnectedEntityType``."""

from typing import Literal, TypeAlias, cast

ConnectedEntityType: TypeAlias = Literal["DBMS",]


# --- restJson1 ser/de ---
def serialize_json(value: ConnectedEntityType) -> str:
    return value


def deserialize_json(data: str) -> ConnectedEntityType:
    return cast(ConnectedEntityType, data)
