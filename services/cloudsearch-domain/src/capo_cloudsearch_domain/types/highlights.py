"""Generated from Smithy shape ``com.amazonaws.cloudsearchdomain#Highlights``."""

from typing import TYPE_CHECKING, TypeAlias

if TYPE_CHECKING:
    import capo_cloudsearch_domain.types.string

Highlights: TypeAlias = dict[
    "capo_cloudsearch_domain.types.string.String",
    "capo_cloudsearch_domain.types.string.String",
]


# --- restJson1 ser/de ---
def serialize_json(input_to_serialize: Highlights) -> dict:
    out: dict = {}
    for key, value in input_to_serialize.items():
        out[key] = value
    return out


def deserialize_json(data: dict) -> Highlights:
    out: Highlights = {}
    for key, value in data.items():
        out[key] = value
    return out
