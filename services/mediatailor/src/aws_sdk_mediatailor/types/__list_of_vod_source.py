"""Generated from Smithy shape ``com.amazonaws.mediatailor#__listOfVodSource``."""

from typing import TYPE_CHECKING, TypeAlias

if TYPE_CHECKING:
    import aws_sdk_mediatailor.types.vod_source

__listOfVodSource: TypeAlias = list["aws_sdk_mediatailor.types.vod_source.VodSource"]


# --- restJson1 ser/de ---
def serialize_json(value: __listOfVodSource) -> list:
    import aws_sdk_mediatailor.types.vod_source

    out: list = []
    for item in value:
        out.append(aws_sdk_mediatailor.types.vod_source.serialize_json(item))
    return out


def deserialize_json(data: list) -> __listOfVodSource:
    import aws_sdk_mediatailor.types.vod_source

    out: __listOfVodSource = []
    for item in data:
        out.append(aws_sdk_mediatailor.types.vod_source.deserialize_json(item))
    return out
