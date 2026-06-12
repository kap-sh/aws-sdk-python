"""Generated from Smithy shape ``com.amazonaws.cloudwatchevents#ApiDestinationResponseList``."""

from typing import TYPE_CHECKING, TypeAlias

if TYPE_CHECKING:
    import aws_sdk_cloudwatch_events.types.api_destination

ApiDestinationResponseList: TypeAlias = list[
    "aws_sdk_cloudwatch_events.types.api_destination.ApiDestination"
]


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: ApiDestinationResponseList) -> list:
    import aws_sdk_cloudwatch_events.types.api_destination

    out: list = []
    for item in value:
        out.append(
            aws_sdk_cloudwatch_events.types.api_destination.serialize_aws_json_1_1(item)
        )
    return out


def deserialize_aws_json_1_1(data: list) -> ApiDestinationResponseList:
    import aws_sdk_cloudwatch_events.types.api_destination

    out: ApiDestinationResponseList = []
    for item in data:
        out.append(
            aws_sdk_cloudwatch_events.types.api_destination.deserialize_aws_json_1_1(
                item
            )
        )
    return out
