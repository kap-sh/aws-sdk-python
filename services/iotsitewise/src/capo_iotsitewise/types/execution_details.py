"""Generated from Smithy shape ``com.amazonaws.iotsitewise#ExecutionDetails``."""

from typing import TYPE_CHECKING, TypeAlias

if TYPE_CHECKING:
    import capo_iotsitewise.types.execution_details_key
    import capo_iotsitewise.types.execution_details_value

ExecutionDetails: TypeAlias = dict[
    "capo_iotsitewise.types.execution_details_key.ExecutionDetailsKey",
    "capo_iotsitewise.types.execution_details_value.ExecutionDetailsValue",
]


# --- restJson1 ser/de ---
def serialize_json(input_to_serialize: ExecutionDetails) -> dict:
    out: dict = {}
    for key, value in input_to_serialize.items():
        out[key] = value
    return out


def deserialize_json(data: dict) -> ExecutionDetails:
    out: ExecutionDetails = {}
    for key, value in data.items():
        out[key] = value
    return out
