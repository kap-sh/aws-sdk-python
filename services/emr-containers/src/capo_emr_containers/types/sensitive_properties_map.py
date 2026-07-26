"""Generated from Smithy shape ``com.amazonaws.emrcontainers#SensitivePropertiesMap``."""

from typing import TYPE_CHECKING, TypeAlias

if TYPE_CHECKING:
    import capo_emr_containers.types.string1024

SensitivePropertiesMap: TypeAlias = dict[
    "capo_emr_containers.types.string1024.String1024",
    "capo_emr_containers.types.string1024.String1024",
]


# --- restJson1 ser/de ---
def serialize_json(input_to_serialize: SensitivePropertiesMap) -> dict:
    out: dict = {}
    for key, value in input_to_serialize.items():
        out[key] = value
    return out


def deserialize_json(data: dict) -> SensitivePropertiesMap:
    out: SensitivePropertiesMap = {}
    for key, value in data.items():
        out[key] = value
    return out
