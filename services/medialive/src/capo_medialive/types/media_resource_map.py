"""Generated from Smithy shape ``com.amazonaws.medialive#MediaResourceMap``."""

from typing import TYPE_CHECKING, TypeAlias

if TYPE_CHECKING:
    import capo_medialive.types.__string
    import capo_medialive.types.media_resource

MediaResourceMap: TypeAlias = dict[
    "capo_medialive.types.__string.__string",
    "capo_medialive.types.media_resource.MediaResource",
]


# --- restJson1 ser/de ---
def serialize_json(input_to_serialize: MediaResourceMap) -> dict:
    out: dict = {}
    for key, value in input_to_serialize.items():
        import capo_medialive.types.media_resource

        out[key] = capo_medialive.types.media_resource.serialize_json(value)
    return out


def deserialize_json(data: dict) -> MediaResourceMap:
    out: MediaResourceMap = {}
    for key, value in data.items():
        import capo_medialive.types.media_resource

        out[key] = capo_medialive.types.media_resource.deserialize_json(value)
    return out
