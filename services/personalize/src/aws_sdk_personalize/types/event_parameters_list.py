"""Generated from Smithy shape ``com.amazonaws.personalize#EventParametersList``."""

from typing import TYPE_CHECKING, TypeAlias

if TYPE_CHECKING:
    import aws_sdk_personalize.types.event_parameters

EventParametersList: TypeAlias = list[
    "aws_sdk_personalize.types.event_parameters.EventParameters"
]


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: EventParametersList) -> list:
    import aws_sdk_personalize.types.event_parameters

    out: list = []
    for item in value:
        out.append(
            aws_sdk_personalize.types.event_parameters.serialize_aws_json_1_1(item)
        )
    return out


def deserialize_aws_json_1_1(data: list) -> EventParametersList:
    import aws_sdk_personalize.types.event_parameters

    out: EventParametersList = []
    for item in data:
        out.append(
            aws_sdk_personalize.types.event_parameters.deserialize_aws_json_1_1(item)
        )
    return out
