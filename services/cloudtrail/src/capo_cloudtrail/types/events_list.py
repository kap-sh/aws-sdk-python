"""Generated from Smithy shape ``com.amazonaws.cloudtrail#EventsList``."""

from typing import TYPE_CHECKING, TypeAlias

if TYPE_CHECKING:
    import capo_cloudtrail.types.event

EventsList: TypeAlias = list["capo_cloudtrail.types.event.Event"]


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: EventsList) -> list:
    import capo_cloudtrail.types.event

    out: list = []
    for item in value:
        out.append(capo_cloudtrail.types.event.serialize_aws_json_1_1(item))
    return out


def deserialize_aws_json_1_1(data: list) -> EventsList:
    import capo_cloudtrail.types.event

    out: EventsList = []
    for item in data:
        out.append(capo_cloudtrail.types.event.deserialize_aws_json_1_1(item))
    return out
