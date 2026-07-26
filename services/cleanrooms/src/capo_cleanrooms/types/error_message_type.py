"""Generated from Smithy shape ``com.amazonaws.cleanrooms#ErrorMessageType``."""

from typing import Literal, TypeAlias, cast

ErrorMessageType: TypeAlias = Literal["DETAILED",]


# --- restJson1 ser/de ---
def serialize_json(value: ErrorMessageType) -> str:
    return value


def deserialize_json(data: str) -> ErrorMessageType:
    return cast(ErrorMessageType, data)
