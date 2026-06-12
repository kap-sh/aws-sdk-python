"""Generated from Smithy shape ``com.amazonaws.cloudtrail#EventSelectors``."""

from typing import TYPE_CHECKING, TypeAlias

if TYPE_CHECKING:
    import aws_sdk_cloudtrail.types.event_selector

EventSelectors: TypeAlias = list[
    "aws_sdk_cloudtrail.types.event_selector.EventSelector"
]


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: EventSelectors) -> list:
    import aws_sdk_cloudtrail.types.event_selector

    out: list = []
    for item in value:
        out.append(aws_sdk_cloudtrail.types.event_selector.serialize_aws_json_1_1(item))
    return out


def deserialize_aws_json_1_1(data: list) -> EventSelectors:
    import aws_sdk_cloudtrail.types.event_selector

    out: EventSelectors = []
    for item in data:
        out.append(
            aws_sdk_cloudtrail.types.event_selector.deserialize_aws_json_1_1(item)
        )
    return out
