"""Generated from Smithy shape ``com.amazonaws.amplify#BuildComputeType``."""

from typing import Literal, TypeAlias, cast

BuildComputeType: TypeAlias = Literal[
    "STANDARD_8GB",
    "LARGE_16GB",
    "XLARGE_72GB",
]


# --- restJson1 ser/de ---
def serialize_json(value: BuildComputeType) -> str:
    return value


def deserialize_json(data: str) -> BuildComputeType:
    return cast(BuildComputeType, data)
