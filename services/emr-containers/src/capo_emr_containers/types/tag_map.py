"""Generated from Smithy shape ``com.amazonaws.emrcontainers#TagMap``."""

from typing import TYPE_CHECKING, TypeAlias

if TYPE_CHECKING:
    import capo_emr_containers.types.string128
    import capo_emr_containers.types.string_empty256

TagMap: TypeAlias = dict[
    "capo_emr_containers.types.string128.String128",
    "capo_emr_containers.types.string_empty256.StringEmpty256",
]


# --- restJson1 ser/de ---
def serialize_json(input_to_serialize: TagMap) -> dict:
    out: dict = {}
    for key, value in input_to_serialize.items():
        out[key] = value
    return out


def deserialize_json(data: dict) -> TagMap:
    out: TagMap = {}
    for key, value in data.items():
        out[key] = value
    return out
