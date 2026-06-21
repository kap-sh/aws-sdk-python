"""Generated from Smithy shape ``com.amazonaws.kinesisvideomedia#StartSelectorType``."""

from typing import Literal, TypeAlias, cast

StartSelectorType: TypeAlias = Literal[
    "FRAGMENT_NUMBER",
    "SERVER_TIMESTAMP",
    "PRODUCER_TIMESTAMP",
    "NOW",
    "EARLIEST",
    "CONTINUATION_TOKEN",
]


# --- restJson1 ser/de ---
def serialize_json(value: StartSelectorType) -> str:
    return value


def deserialize_json(data: str) -> StartSelectorType:
    return cast(StartSelectorType, data)
