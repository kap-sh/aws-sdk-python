"""Generated from Smithy shape ``com.amazonaws.sagemakeredge#ModelState``."""

from typing import Literal, TypeAlias, cast

ModelState: TypeAlias = Literal[
    "DEPLOY",
    "UNDEPLOY",
]


# --- restJson1 ser/de ---
def serialize_json(value: ModelState) -> str:
    return value


def deserialize_json(data: str) -> ModelState:
    return cast(ModelState, data)
