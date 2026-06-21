"""Generated from Smithy shape ``com.amazonaws.iotsitewise#DetailedErrorCode``."""

from typing import Literal, TypeAlias, cast

DetailedErrorCode: TypeAlias = Literal[
    "INCOMPATIBLE_COMPUTE_LOCATION",
    "INCOMPATIBLE_FORWARDING_CONFIGURATION",
]


# --- restJson1 ser/de ---
def serialize_json(value: DetailedErrorCode) -> str:
    return value


def deserialize_json(data: str) -> DetailedErrorCode:
    return cast(DetailedErrorCode, data)
