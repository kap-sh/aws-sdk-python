"""Generated from Smithy shape ``com.amazonaws.pcaconnectorad#ClientCompatibilityV2``."""

from typing import Literal, TypeAlias, cast

ClientCompatibilityV2: TypeAlias = Literal[
    "WINDOWS_SERVER_2003",
    "WINDOWS_SERVER_2008",
    "WINDOWS_SERVER_2008_R2",
    "WINDOWS_SERVER_2012",
    "WINDOWS_SERVER_2012_R2",
    "WINDOWS_SERVER_2016",
]


# --- restJson1 ser/de ---
def serialize_json(value: ClientCompatibilityV2) -> str:
    return value


def deserialize_json(data: str) -> ClientCompatibilityV2:
    return cast(ClientCompatibilityV2, data)
