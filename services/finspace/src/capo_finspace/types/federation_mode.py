"""Generated from Smithy shape ``com.amazonaws.finspace#FederationMode``."""

from typing import Literal, TypeAlias, cast

FederationMode: TypeAlias = Literal[
    "FEDERATED",
    "LOCAL",
]


# --- restJson1 ser/de ---
def serialize_json(value: FederationMode) -> str:
    return value


def deserialize_json(data: str) -> FederationMode:
    return cast(FederationMode, data)
