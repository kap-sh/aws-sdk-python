"""Generated from Smithy shape ``com.amazonaws.qapps#InputCardComputeMode``."""

from typing import Literal, TypeAlias, cast

InputCardComputeMode: TypeAlias = Literal[
    "append",
    "replace",
]


# --- restJson1 ser/de ---
def serialize_json(value: InputCardComputeMode) -> str:
    return value


def deserialize_json(data: str) -> InputCardComputeMode:
    return cast(InputCardComputeMode, data)
