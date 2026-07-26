"""Generated from Smithy shape ``com.amazonaws.datazone#ComputeEnvironments``."""

from typing import Literal, TypeAlias, cast

ComputeEnvironments: TypeAlias = Literal[
    "SPARK",
    "ATHENA",
    "PYTHON",
]


# --- restJson1 ser/de ---
def serialize_json(value: ComputeEnvironments) -> str:
    return value


def deserialize_json(data: str) -> ComputeEnvironments:
    return cast(ComputeEnvironments, data)
