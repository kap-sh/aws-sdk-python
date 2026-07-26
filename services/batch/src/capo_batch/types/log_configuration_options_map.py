"""Generated from Smithy shape ``com.amazonaws.batch#LogConfigurationOptionsMap``."""

from typing import TYPE_CHECKING, TypeAlias

if TYPE_CHECKING:
    import capo_batch.types.string

LogConfigurationOptionsMap: TypeAlias = dict[
    "capo_batch.types.string.String", "capo_batch.types.string.String"
]


# --- restJson1 ser/de ---
def serialize_json(input_to_serialize: LogConfigurationOptionsMap) -> dict:
    out: dict = {}
    for key, value in input_to_serialize.items():
        out[key] = value
    return out


def deserialize_json(data: dict) -> LogConfigurationOptionsMap:
    out: LogConfigurationOptionsMap = {}
    for key, value in data.items():
        out[key] = value
    return out
