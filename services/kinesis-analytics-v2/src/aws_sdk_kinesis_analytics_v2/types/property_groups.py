"""Generated from Smithy shape ``com.amazonaws.kinesisanalyticsv2#PropertyGroups``."""

from typing import TYPE_CHECKING, TypeAlias

if TYPE_CHECKING:
    import aws_sdk_kinesis_analytics_v2.types.property_group

PropertyGroups: TypeAlias = list[
    "aws_sdk_kinesis_analytics_v2.types.property_group.PropertyGroup"
]


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: PropertyGroups) -> list:
    import aws_sdk_kinesis_analytics_v2.types.property_group

    out: list = []
    for item in value:
        out.append(
            aws_sdk_kinesis_analytics_v2.types.property_group.serialize_aws_json_1_1(
                item
            )
        )
    return out


def deserialize_aws_json_1_1(data: list) -> PropertyGroups:
    import aws_sdk_kinesis_analytics_v2.types.property_group

    out: PropertyGroups = []
    for item in data:
        out.append(
            aws_sdk_kinesis_analytics_v2.types.property_group.deserialize_aws_json_1_1(
                item
            )
        )
    return out
