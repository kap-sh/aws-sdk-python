"""Generated from Smithy shape ``com.amazonaws.health#EventTypeActionabilityList``."""

from typing import TYPE_CHECKING, TypeAlias

if TYPE_CHECKING:
    import aws_sdk_health.types.event_type_actionability

EventTypeActionabilityList: TypeAlias = list[
    "aws_sdk_health.types.event_type_actionability.EventTypeActionability"
]


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: EventTypeActionabilityList) -> list:
    import aws_sdk_health.types.event_type_actionability

    out: list = []
    for item in value:
        out.append(
            aws_sdk_health.types.event_type_actionability.serialize_aws_json_1_1(item)
        )
    return out


def deserialize_aws_json_1_1(data: list) -> EventTypeActionabilityList:
    import aws_sdk_health.types.event_type_actionability

    out: EventTypeActionabilityList = []
    for item in data:
        out.append(
            aws_sdk_health.types.event_type_actionability.deserialize_aws_json_1_1(item)
        )
    return out
