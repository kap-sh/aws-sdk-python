"""Generated from Smithy shape ``com.amazonaws.pcaconnectorad#ClientCompatibilityV4``."""

from typing import Literal, TypeAlias, cast

ClientCompatibilityV4: TypeAlias = Literal[
    "WINDOWS_SERVER_2012",
    "WINDOWS_SERVER_2012_R2",
    "WINDOWS_SERVER_2016",
]


# --- restJson1 ser/de ---
def serialize_json(value: ClientCompatibilityV4) -> str:
    return value


def deserialize_json(data: str) -> ClientCompatibilityV4:
    return cast(ClientCompatibilityV4, data)
