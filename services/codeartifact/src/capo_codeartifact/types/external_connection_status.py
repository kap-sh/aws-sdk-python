"""Generated from Smithy shape ``com.amazonaws.codeartifact#ExternalConnectionStatus``."""

from typing import Literal, TypeAlias, cast

ExternalConnectionStatus: TypeAlias = Literal["Available",]


# --- restJson1 ser/de ---
def serialize_json(value: ExternalConnectionStatus) -> str:
    return value


def deserialize_json(data: str) -> ExternalConnectionStatus:
    return cast(ExternalConnectionStatus, data)
