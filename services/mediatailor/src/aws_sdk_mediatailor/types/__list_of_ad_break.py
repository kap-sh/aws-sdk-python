"""Generated from Smithy shape ``com.amazonaws.mediatailor#__listOfAdBreak``."""

from typing import TYPE_CHECKING, TypeAlias

if TYPE_CHECKING:
    import aws_sdk_mediatailor.types.ad_break

__listOfAdBreak: TypeAlias = list["aws_sdk_mediatailor.types.ad_break.AdBreak"]


# --- restJson1 ser/de ---
def serialize_json(value: __listOfAdBreak) -> list:
    import aws_sdk_mediatailor.types.ad_break

    out: list = []
    for item in value:
        out.append(aws_sdk_mediatailor.types.ad_break.serialize_json(item))
    return out


def deserialize_json(data: list) -> __listOfAdBreak:
    import aws_sdk_mediatailor.types.ad_break

    out: __listOfAdBreak = []
    for item in data:
        out.append(aws_sdk_mediatailor.types.ad_break.deserialize_json(item))
    return out
