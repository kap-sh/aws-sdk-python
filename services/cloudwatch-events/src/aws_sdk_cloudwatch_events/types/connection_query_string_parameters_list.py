"""Generated from Smithy shape ``com.amazonaws.cloudwatchevents#ConnectionQueryStringParametersList``."""

from typing import TYPE_CHECKING, TypeAlias

if TYPE_CHECKING:
    import aws_sdk_cloudwatch_events.types.connection_query_string_parameter

ConnectionQueryStringParametersList: TypeAlias = list[
    "aws_sdk_cloudwatch_events.types.connection_query_string_parameter.ConnectionQueryStringParameter"
]


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: ConnectionQueryStringParametersList) -> list:
    import aws_sdk_cloudwatch_events.types.connection_query_string_parameter

    out: list = []
    for item in value:
        out.append(
            aws_sdk_cloudwatch_events.types.connection_query_string_parameter.serialize_aws_json_1_1(
                item
            )
        )
    return out


def deserialize_aws_json_1_1(data: list) -> ConnectionQueryStringParametersList:
    import aws_sdk_cloudwatch_events.types.connection_query_string_parameter

    out: ConnectionQueryStringParametersList = []
    for item in data:
        out.append(
            aws_sdk_cloudwatch_events.types.connection_query_string_parameter.deserialize_aws_json_1_1(
                item
            )
        )
    return out
