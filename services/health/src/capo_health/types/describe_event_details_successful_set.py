"""Generated from Smithy shape ``com.amazonaws.health#DescribeEventDetailsSuccessfulSet``."""

from typing import TYPE_CHECKING, TypeAlias

if TYPE_CHECKING:
    import capo_health.types.event_details

DescribeEventDetailsSuccessfulSet: TypeAlias = list[
    "capo_health.types.event_details.EventDetails"
]


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: DescribeEventDetailsSuccessfulSet) -> list:
    import capo_health.types.event_details

    out: list = []
    for item in value:
        out.append(capo_health.types.event_details.serialize_aws_json_1_1(item))
    return out


def deserialize_aws_json_1_1(data: list) -> DescribeEventDetailsSuccessfulSet:
    import capo_health.types.event_details

    out: DescribeEventDetailsSuccessfulSet = []
    for item in data:
        out.append(capo_health.types.event_details.deserialize_aws_json_1_1(item))
    return out
