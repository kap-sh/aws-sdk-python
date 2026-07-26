"""Generated from Smithy shape ``com.amazonaws.inspector2#StopCisSessionStatus``."""

from typing import Literal, TypeAlias, cast

StopCisSessionStatus: TypeAlias = Literal[
    "SUCCESS",
    "FAILED",
    "INTERRUPTED",
    "UNSUPPORTED_OS",
]


# --- restJson1 ser/de ---
def serialize_json(value: StopCisSessionStatus) -> str:
    return value


def deserialize_json(data: str) -> StopCisSessionStatus:
    return cast(StopCisSessionStatus, data)
