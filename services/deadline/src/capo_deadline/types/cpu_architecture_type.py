"""Generated from Smithy shape ``com.amazonaws.deadline#CpuArchitectureType``."""

from typing import Literal, TypeAlias, cast

CpuArchitectureType: TypeAlias = Literal[
    "x86_64",
    "arm64",
]


# --- restJson1 ser/de ---
def serialize_json(value: CpuArchitectureType) -> str:
    return value


def deserialize_json(data: str) -> CpuArchitectureType:
    return cast(CpuArchitectureType, data)
