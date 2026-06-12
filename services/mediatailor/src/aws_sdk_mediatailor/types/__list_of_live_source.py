"""Generated from Smithy shape ``com.amazonaws.mediatailor#__listOfLiveSource``."""

from typing import TYPE_CHECKING, TypeAlias

if TYPE_CHECKING:
    import aws_sdk_mediatailor.types.live_source

__listOfLiveSource: TypeAlias = list["aws_sdk_mediatailor.types.live_source.LiveSource"]


# --- restJson1 ser/de ---
def serialize_json(value: __listOfLiveSource) -> list:
    import aws_sdk_mediatailor.types.live_source

    out: list = []
    for item in value:
        out.append(aws_sdk_mediatailor.types.live_source.serialize_json(item))
    return out


def deserialize_json(data: list) -> __listOfLiveSource:
    import aws_sdk_mediatailor.types.live_source

    out: __listOfLiveSource = []
    for item in data:
        out.append(aws_sdk_mediatailor.types.live_source.deserialize_json(item))
    return out
