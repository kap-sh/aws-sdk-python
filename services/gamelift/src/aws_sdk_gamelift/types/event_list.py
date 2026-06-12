"""Generated from Smithy shape ``com.amazonaws.gamelift#EventList``."""

from typing import TYPE_CHECKING, TypeAlias

if TYPE_CHECKING:
    import aws_sdk_gamelift.types.event

EventList: TypeAlias = list["aws_sdk_gamelift.types.event.Event"]


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: EventList) -> list:
    import aws_sdk_gamelift.types.event

    out: list = []
    for item in value:
        out.append(aws_sdk_gamelift.types.event.serialize_aws_json_1_1(item))
    return out


def deserialize_aws_json_1_1(data: list) -> EventList:
    import aws_sdk_gamelift.types.event

    out: EventList = []
    for item in data:
        out.append(aws_sdk_gamelift.types.event.deserialize_aws_json_1_1(item))
    return out
