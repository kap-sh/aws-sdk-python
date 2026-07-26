"""Generated from Smithy shape ``com.amazonaws.elasticsearchservice#AdvancedOptions``."""

from typing import TYPE_CHECKING, TypeAlias

if TYPE_CHECKING:
    import capo_elasticsearch_service.types.string

AdvancedOptions: TypeAlias = dict[
    "capo_elasticsearch_service.types.string.String",
    "capo_elasticsearch_service.types.string.String",
]


# --- restJson1 ser/de ---
def serialize_json(input_to_serialize: AdvancedOptions) -> dict:
    out: dict = {}
    for key, value in input_to_serialize.items():
        out[key] = value
    return out


def deserialize_json(data: dict) -> AdvancedOptions:
    out: AdvancedOptions = {}
    for key, value in data.items():
        out[key] = value
    return out
