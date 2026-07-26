"""Generated from Smithy shape ``com.amazonaws.sagemakerfeaturestoreruntime#ExpirationTimeResponse``."""

from typing import Literal, TypeAlias, cast

ExpirationTimeResponse: TypeAlias = Literal[
    "Enabled",
    "Disabled",
]


# --- restJson1 ser/de ---
def serialize_json(value: ExpirationTimeResponse) -> str:
    return value


def deserialize_json(data: str) -> ExpirationTimeResponse:
    return cast(ExpirationTimeResponse, data)
