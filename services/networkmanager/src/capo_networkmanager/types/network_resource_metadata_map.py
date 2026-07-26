"""Generated from Smithy shape ``com.amazonaws.networkmanager#NetworkResourceMetadataMap``."""

from typing import TYPE_CHECKING, TypeAlias

if TYPE_CHECKING:
    import capo_networkmanager.types.constrained_string

NetworkResourceMetadataMap: TypeAlias = dict[
    "capo_networkmanager.types.constrained_string.ConstrainedString",
    "capo_networkmanager.types.constrained_string.ConstrainedString",
]


# --- restJson1 ser/de ---
def serialize_json(input_to_serialize: NetworkResourceMetadataMap) -> dict:
    out: dict = {}
    for key, value in input_to_serialize.items():
        out[key] = value
    return out


def deserialize_json(data: dict) -> NetworkResourceMetadataMap:
    out: NetworkResourceMetadataMap = {}
    for key, value in data.items():
        out[key] = value
    return out
