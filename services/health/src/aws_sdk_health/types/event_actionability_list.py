"""Generated from Smithy shape ``com.amazonaws.health#EventActionabilityList``."""

from typing import TYPE_CHECKING, TypeAlias

if TYPE_CHECKING:
    import aws_sdk_health.types.event_actionability

EventActionabilityList: TypeAlias = list[
    "aws_sdk_health.types.event_actionability.EventActionability"
]


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: EventActionabilityList) -> list:
    import aws_sdk_health.types.event_actionability

    out: list = []
    for item in value:
        out.append(
            aws_sdk_health.types.event_actionability.serialize_aws_json_1_1(item)
        )
    return out


def deserialize_aws_json_1_1(data: list) -> EventActionabilityList:
    import aws_sdk_health.types.event_actionability

    out: EventActionabilityList = []
    for item in data:
        out.append(
            aws_sdk_health.types.event_actionability.deserialize_aws_json_1_1(item)
        )
    return out
