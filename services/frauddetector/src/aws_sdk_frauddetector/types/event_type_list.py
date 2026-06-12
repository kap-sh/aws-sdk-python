"""Generated from Smithy shape ``com.amazonaws.frauddetector#eventTypeList``."""

from typing import TYPE_CHECKING, TypeAlias

if TYPE_CHECKING:
    import aws_sdk_frauddetector.types.event_type

eventTypeList: TypeAlias = list["aws_sdk_frauddetector.types.event_type.EventType"]


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: eventTypeList) -> list:
    import aws_sdk_frauddetector.types.event_type

    out: list = []
    for item in value:
        out.append(aws_sdk_frauddetector.types.event_type.serialize_aws_json_1_1(item))
    return out


def deserialize_aws_json_1_1(data: list) -> eventTypeList:
    import aws_sdk_frauddetector.types.event_type

    out: eventTypeList = []
    for item in data:
        out.append(
            aws_sdk_frauddetector.types.event_type.deserialize_aws_json_1_1(item)
        )
    return out
