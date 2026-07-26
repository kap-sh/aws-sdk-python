"""Generated from Smithy shape ``com.amazonaws.cloudwatchlogs#Destinations``."""

from typing import TYPE_CHECKING, TypeAlias

if TYPE_CHECKING:
    import capo_cloudwatch_logs.types.destination

Destinations: TypeAlias = list["capo_cloudwatch_logs.types.destination.Destination"]


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: Destinations) -> list:
    import capo_cloudwatch_logs.types.destination

    out: list = []
    for item in value:
        out.append(capo_cloudwatch_logs.types.destination.serialize_aws_json_1_1(item))
    return out


def deserialize_aws_json_1_1(data: list) -> Destinations:
    import capo_cloudwatch_logs.types.destination

    out: Destinations = []
    for item in data:
        out.append(
            capo_cloudwatch_logs.types.destination.deserialize_aws_json_1_1(item)
        )
    return out
