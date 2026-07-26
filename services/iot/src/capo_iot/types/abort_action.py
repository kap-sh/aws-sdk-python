"""Generated from Smithy shape ``com.amazonaws.iot#AbortAction``."""

from typing import Literal, TypeAlias, cast

AbortAction: TypeAlias = Literal["CANCEL",]


# --- restJson1 ser/de ---
def serialize_json(value: AbortAction) -> str:
    return value


def deserialize_json(data: str) -> AbortAction:
    return cast(AbortAction, data)
