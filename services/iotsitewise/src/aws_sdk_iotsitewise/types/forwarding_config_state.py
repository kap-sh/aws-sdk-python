"""Generated from Smithy shape ``com.amazonaws.iotsitewise#ForwardingConfigState``."""

from typing import Literal, TypeAlias, cast

ForwardingConfigState: TypeAlias = Literal[
    "DISABLED",
    "ENABLED",
]


# --- restJson1 ser/de ---
def serialize_json(value: ForwardingConfigState) -> str:
    return value


def deserialize_json(data: str) -> ForwardingConfigState:
    return cast(ForwardingConfigState, data)
