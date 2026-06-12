"""Generated from Smithy shape ``com.amazonaws.medialive#__listOfMultiplexAlert``."""

from typing import TYPE_CHECKING, TypeAlias

if TYPE_CHECKING:
    import aws_sdk_medialive.types.multiplex_alert

__listOfMultiplexAlert: TypeAlias = list[
    "aws_sdk_medialive.types.multiplex_alert.MultiplexAlert"
]


# --- restJson1 ser/de ---
def serialize_json(value: __listOfMultiplexAlert) -> list:
    import aws_sdk_medialive.types.multiplex_alert

    out: list = []
    for item in value:
        out.append(aws_sdk_medialive.types.multiplex_alert.serialize_json(item))
    return out


def deserialize_json(data: list) -> __listOfMultiplexAlert:
    import aws_sdk_medialive.types.multiplex_alert

    out: __listOfMultiplexAlert = []
    for item in data:
        out.append(aws_sdk_medialive.types.multiplex_alert.deserialize_json(item))
    return out
