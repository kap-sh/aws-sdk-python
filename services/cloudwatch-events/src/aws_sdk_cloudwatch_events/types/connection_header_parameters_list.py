"""Generated from Smithy shape ``com.amazonaws.cloudwatchevents#ConnectionHeaderParametersList``."""

from typing import TYPE_CHECKING, TypeAlias

if TYPE_CHECKING:
    import aws_sdk_cloudwatch_events.types.connection_header_parameter

ConnectionHeaderParametersList: TypeAlias = list[
    "aws_sdk_cloudwatch_events.types.connection_header_parameter.ConnectionHeaderParameter"
]


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: ConnectionHeaderParametersList) -> list:
    import aws_sdk_cloudwatch_events.types.connection_header_parameter

    out: list = []
    for item in value:
        out.append(
            aws_sdk_cloudwatch_events.types.connection_header_parameter.serialize_aws_json_1_1(
                item
            )
        )
    return out


def deserialize_aws_json_1_1(data: list) -> ConnectionHeaderParametersList:
    import aws_sdk_cloudwatch_events.types.connection_header_parameter

    out: ConnectionHeaderParametersList = []
    for item in data:
        out.append(
            aws_sdk_cloudwatch_events.types.connection_header_parameter.deserialize_aws_json_1_1(
                item
            )
        )
    return out
