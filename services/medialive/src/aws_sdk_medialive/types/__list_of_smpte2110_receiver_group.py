"""Generated from Smithy shape ``com.amazonaws.medialive#__listOfSmpte2110ReceiverGroup``."""

from typing import TYPE_CHECKING, TypeAlias

if TYPE_CHECKING:
    import aws_sdk_medialive.types.smpte2110_receiver_group

__listOfSmpte2110ReceiverGroup: TypeAlias = list[
    "aws_sdk_medialive.types.smpte2110_receiver_group.Smpte2110ReceiverGroup"
]


# --- restJson1 ser/de ---
def serialize_json(value: __listOfSmpte2110ReceiverGroup) -> list:
    import aws_sdk_medialive.types.smpte2110_receiver_group

    out: list = []
    for item in value:
        out.append(
            aws_sdk_medialive.types.smpte2110_receiver_group.serialize_json(item)
        )
    return out


def deserialize_json(data: list) -> __listOfSmpte2110ReceiverGroup:
    import aws_sdk_medialive.types.smpte2110_receiver_group

    out: __listOfSmpte2110ReceiverGroup = []
    for item in data:
        out.append(
            aws_sdk_medialive.types.smpte2110_receiver_group.deserialize_json(item)
        )
    return out
