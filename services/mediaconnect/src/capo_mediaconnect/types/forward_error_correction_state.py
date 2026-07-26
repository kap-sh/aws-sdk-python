"""Generated from Smithy shape ``com.amazonaws.mediaconnect#ForwardErrorCorrectionState``."""

from typing import Literal, TypeAlias, cast

ForwardErrorCorrectionState: TypeAlias = Literal[
    "ENABLED",
    "DISABLED",
]


# --- restJson1 ser/de ---
def serialize_json(value: ForwardErrorCorrectionState) -> str:
    return value


def deserialize_json(data: str) -> ForwardErrorCorrectionState:
    return cast(ForwardErrorCorrectionState, data)
