"""Generated from Smithy shape ``com.amazonaws.chimesdkvoice#CallingRegionList``."""

from typing import TYPE_CHECKING, TypeAlias

if TYPE_CHECKING:
    import aws_sdk_chime_sdk_voice.types.calling_region

CallingRegionList: TypeAlias = list[
    "aws_sdk_chime_sdk_voice.types.calling_region.CallingRegion"
]


# --- restJson1 ser/de ---
def serialize_json(value: CallingRegionList) -> list:
    return list(value)


def deserialize_json(data: list) -> CallingRegionList:
    return list(data)
