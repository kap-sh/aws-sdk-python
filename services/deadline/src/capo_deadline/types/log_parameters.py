"""Generated from Smithy shape ``com.amazonaws.deadline#LogParameters``."""

from typing import TYPE_CHECKING, TypeAlias

if TYPE_CHECKING:
    import capo_deadline.types.string

LogParameters: TypeAlias = dict[
    "capo_deadline.types.string.String", "capo_deadline.types.string.String"
]


# --- restJson1 ser/de ---
def serialize_json(input_to_serialize: LogParameters) -> dict:
    out: dict = {}
    for key, value in input_to_serialize.items():
        out[key] = value
    return out


def deserialize_json(data: dict) -> LogParameters:
    out: LogParameters = {}
    for key, value in data.items():
        out[key] = value
    return out
