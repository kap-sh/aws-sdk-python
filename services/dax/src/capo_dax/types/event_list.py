"""Generated from Smithy shape ``com.amazonaws.dax#EventList``."""

from typing import TYPE_CHECKING, TypeAlias

if TYPE_CHECKING:
    import capo_dax.types.event

EventList: TypeAlias = list["capo_dax.types.event.Event"]


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: EventList) -> list:
    import capo_dax.types.event

    out: list = []
    for item in value:
        out.append(capo_dax.types.event.serialize_aws_json_1_1(item))
    return out


def deserialize_aws_json_1_1(data: list) -> EventList:
    import capo_dax.types.event

    out: EventList = []
    for item in data:
        out.append(capo_dax.types.event.deserialize_aws_json_1_1(item))
    return out
