"""Generated from Smithy shape ``com.amazonaws.mediatailor#__listOfVodSource``."""

from typing import TYPE_CHECKING, TypeAlias

if TYPE_CHECKING:
    import capo_mediatailor.types.vod_source

__listOfVodSource: TypeAlias = list["capo_mediatailor.types.vod_source.VodSource"]


# --- restJson1 ser/de ---
def serialize_json(value: __listOfVodSource) -> list:
    import capo_mediatailor.types.vod_source

    out: list = []
    for item in value:
        out.append(capo_mediatailor.types.vod_source.serialize_json(item))
    return out


def deserialize_json(data: list) -> __listOfVodSource:
    import capo_mediatailor.types.vod_source

    out: __listOfVodSource = []
    for item in data:
        out.append(capo_mediatailor.types.vod_source.deserialize_json(item))
    return out
