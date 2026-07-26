"""Generated from Smithy shape ``com.amazonaws.cloudwatchevents#ConnectionBodyParametersList``."""

from typing import TYPE_CHECKING, TypeAlias

if TYPE_CHECKING:
    import capo_cloudwatch_events.types.connection_body_parameter

ConnectionBodyParametersList: TypeAlias = list[
    "capo_cloudwatch_events.types.connection_body_parameter.ConnectionBodyParameter"
]


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: ConnectionBodyParametersList) -> list:
    import capo_cloudwatch_events.types.connection_body_parameter

    out: list = []
    for item in value:
        out.append(
            capo_cloudwatch_events.types.connection_body_parameter.serialize_aws_json_1_1(
                item
            )
        )
    return out


def deserialize_aws_json_1_1(data: list) -> ConnectionBodyParametersList:
    import capo_cloudwatch_events.types.connection_body_parameter

    out: ConnectionBodyParametersList = []
    for item in data:
        out.append(
            capo_cloudwatch_events.types.connection_body_parameter.deserialize_aws_json_1_1(
                item
            )
        )
    return out
