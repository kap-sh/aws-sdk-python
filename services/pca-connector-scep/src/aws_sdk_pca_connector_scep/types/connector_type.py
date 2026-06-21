"""Generated from Smithy shape ``com.amazonaws.pcaconnectorscep#ConnectorType``."""

from typing import Literal, TypeAlias, cast

ConnectorType: TypeAlias = Literal[
    "GENERAL_PURPOSE",
    "INTUNE",
]


# --- restJson1 ser/de ---
def serialize_json(value: ConnectorType) -> str:
    return value


def deserialize_json(data: str) -> ConnectorType:
    return cast(ConnectorType, data)
