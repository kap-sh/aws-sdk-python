"""Generated from Smithy shape ``com.amazonaws.medialive#SdiSourceMappings``."""

from typing import TYPE_CHECKING, TypeAlias

if TYPE_CHECKING:
    import capo_medialive.types.sdi_source_mapping

SdiSourceMappings: TypeAlias = list[
    "capo_medialive.types.sdi_source_mapping.SdiSourceMapping"
]


# --- restJson1 ser/de ---
def serialize_json(value: SdiSourceMappings) -> list:
    import capo_medialive.types.sdi_source_mapping

    out: list = []
    for item in value:
        out.append(capo_medialive.types.sdi_source_mapping.serialize_json(item))
    return out


def deserialize_json(data: list) -> SdiSourceMappings:
    import capo_medialive.types.sdi_source_mapping

    out: SdiSourceMappings = []
    for item in data:
        out.append(capo_medialive.types.sdi_source_mapping.deserialize_json(item))
    return out
