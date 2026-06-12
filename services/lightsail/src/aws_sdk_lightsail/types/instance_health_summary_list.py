"""Generated from Smithy shape ``com.amazonaws.lightsail#InstanceHealthSummaryList``."""

from typing import TYPE_CHECKING, TypeAlias

if TYPE_CHECKING:
    import aws_sdk_lightsail.types.instance_health_summary

InstanceHealthSummaryList: TypeAlias = list[
    "aws_sdk_lightsail.types.instance_health_summary.InstanceHealthSummary"
]


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: InstanceHealthSummaryList) -> list:
    import aws_sdk_lightsail.types.instance_health_summary

    out: list = []
    for item in value:
        out.append(
            aws_sdk_lightsail.types.instance_health_summary.serialize_aws_json_1_1(item)
        )
    return out


def deserialize_aws_json_1_1(data: list) -> InstanceHealthSummaryList:
    import aws_sdk_lightsail.types.instance_health_summary

    out: InstanceHealthSummaryList = []
    for item in data:
        out.append(
            aws_sdk_lightsail.types.instance_health_summary.deserialize_aws_json_1_1(
                item
            )
        )
    return out
