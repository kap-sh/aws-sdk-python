"""Generated from Smithy shape ``com.amazonaws.rtbfabric#ResponderErrorMaskingLoggingType``."""

from typing import Literal, TypeAlias, cast

ResponderErrorMaskingLoggingType: TypeAlias = Literal[
    "NONE",
    "METRIC",
    "RESPONSE",
]


# --- restJson1 ser/de ---
def serialize_json(value: ResponderErrorMaskingLoggingType) -> str:
    return value


def deserialize_json(data: str) -> ResponderErrorMaskingLoggingType:
    return cast(ResponderErrorMaskingLoggingType, data)
