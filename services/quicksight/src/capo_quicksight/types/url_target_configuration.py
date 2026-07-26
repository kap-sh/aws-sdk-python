"""Generated from Smithy shape ``com.amazonaws.quicksight#URLTargetConfiguration``."""

from typing import Literal, TypeAlias, cast

URLTargetConfiguration: TypeAlias = Literal[
    "NEW_TAB",
    "NEW_WINDOW",
    "SAME_TAB",
]


# --- restJson1 ser/de ---
def serialize_json(value: URLTargetConfiguration) -> str:
    return value


def deserialize_json(data: str) -> URLTargetConfiguration:
    return cast(URLTargetConfiguration, data)
