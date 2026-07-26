"""Generated from Smithy shape ``com.amazonaws.pcaconnectorad#ConnectorStatus``."""

from typing import Literal, TypeAlias, cast

ConnectorStatus: TypeAlias = Literal[
    "CREATING",
    "ACTIVE",
    "DELETING",
    "FAILED",
]


# --- restJson1 ser/de ---
def serialize_json(value: ConnectorStatus) -> str:
    return value


def deserialize_json(data: str) -> ConnectorStatus:
    return cast(ConnectorStatus, data)
