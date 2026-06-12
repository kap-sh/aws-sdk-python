"""Generated from Smithy shape ``com.amazonaws.medialive#__listOfMulticastSource``."""

from typing import TYPE_CHECKING, TypeAlias

if TYPE_CHECKING:
    import aws_sdk_medialive.types.multicast_source

__listOfMulticastSource: TypeAlias = list[
    "aws_sdk_medialive.types.multicast_source.MulticastSource"
]


# --- restJson1 ser/de ---
def serialize_json(value: __listOfMulticastSource) -> list:
    import aws_sdk_medialive.types.multicast_source

    out: list = []
    for item in value:
        out.append(aws_sdk_medialive.types.multicast_source.serialize_json(item))
    return out


def deserialize_json(data: list) -> __listOfMulticastSource:
    import aws_sdk_medialive.types.multicast_source

    out: __listOfMulticastSource = []
    for item in data:
        out.append(aws_sdk_medialive.types.multicast_source.deserialize_json(item))
    return out
