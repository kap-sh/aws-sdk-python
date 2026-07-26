"""Generated from Smithy shape ``com.amazonaws.elastictranscoder#Warnings``."""

from typing import TYPE_CHECKING, TypeAlias

if TYPE_CHECKING:
    import capo_elastic_transcoder.types.warning

Warnings: TypeAlias = list["capo_elastic_transcoder.types.warning.Warning"]


# --- restJson1 ser/de ---
def serialize_json(value: Warnings) -> list:
    import capo_elastic_transcoder.types.warning

    out: list = []
    for item in value:
        out.append(capo_elastic_transcoder.types.warning.serialize_json(item))
    return out


def deserialize_json(data: list) -> Warnings:
    import capo_elastic_transcoder.types.warning

    out: Warnings = []
    for item in data:
        out.append(capo_elastic_transcoder.types.warning.deserialize_json(item))
    return out
