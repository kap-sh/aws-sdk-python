"""Generated from Smithy shape ``com.amazonaws.cloudwatchevents#ConnectionResponseList``."""

from typing import TYPE_CHECKING, TypeAlias

if TYPE_CHECKING:
    import aws_sdk_cloudwatch_events.types.connection

ConnectionResponseList: TypeAlias = list[
    "aws_sdk_cloudwatch_events.types.connection.Connection"
]


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: ConnectionResponseList) -> list:
    import aws_sdk_cloudwatch_events.types.connection

    out: list = []
    for item in value:
        out.append(
            aws_sdk_cloudwatch_events.types.connection.serialize_aws_json_1_1(item)
        )
    return out


def deserialize_aws_json_1_1(data: list) -> ConnectionResponseList:
    import aws_sdk_cloudwatch_events.types.connection

    out: ConnectionResponseList = []
    for item in data:
        out.append(
            aws_sdk_cloudwatch_events.types.connection.deserialize_aws_json_1_1(item)
        )
    return out
