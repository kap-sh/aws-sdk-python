"""Generated from Smithy shape ``com.amazonaws.personalize#EventParametersList``."""

from typing import TYPE_CHECKING, TypeAlias

if TYPE_CHECKING:
    import capo_personalize.types.event_parameters

EventParametersList: TypeAlias = list[
    "capo_personalize.types.event_parameters.EventParameters"
]


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: EventParametersList) -> list:
    import capo_personalize.types.event_parameters

    out: list = []
    for item in value:
        out.append(capo_personalize.types.event_parameters.serialize_aws_json_1_1(item))
    return out


def deserialize_aws_json_1_1(data: list) -> EventParametersList:
    import capo_personalize.types.event_parameters

    out: EventParametersList = []
    for item in data:
        out.append(
            capo_personalize.types.event_parameters.deserialize_aws_json_1_1(item)
        )
    return out
