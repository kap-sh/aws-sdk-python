"""Generated from Smithy shape ``com.amazonaws.connect#ContactMediaProcessingFailureMode``."""

from typing import Literal, TypeAlias, cast

ContactMediaProcessingFailureMode: TypeAlias = Literal[
    "DELIVER_UNPROCESSED_MESSAGE",
    "DO_NOT_DELIVER_UNPROCESSED_MESSAGE",
]


# --- restJson1 ser/de ---
def serialize_json(value: ContactMediaProcessingFailureMode) -> str:
    return value


def deserialize_json(data: str) -> ContactMediaProcessingFailureMode:
    return cast(ContactMediaProcessingFailureMode, data)
