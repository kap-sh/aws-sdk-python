"""Generated from Smithy shape ``com.amazonaws.batch#ArrayJobDependency``."""

from typing import Literal, TypeAlias, cast

ArrayJobDependency: TypeAlias = Literal[
    "N_TO_N",
    "SEQUENTIAL",
]


# --- restJson1 ser/de ---
def serialize_json(value: ArrayJobDependency) -> str:
    return value


def deserialize_json(data: str) -> ArrayJobDependency:
    return cast(ArrayJobDependency, data)
