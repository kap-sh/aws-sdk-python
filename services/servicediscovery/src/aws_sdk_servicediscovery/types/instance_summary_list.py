"""Generated from Smithy shape ``com.amazonaws.servicediscovery#InstanceSummaryList``."""

from typing import TYPE_CHECKING, TypeAlias

if TYPE_CHECKING:
    import aws_sdk_servicediscovery.types.instance_summary

InstanceSummaryList: TypeAlias = list[
    "aws_sdk_servicediscovery.types.instance_summary.InstanceSummary"
]


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: InstanceSummaryList) -> list:
    import aws_sdk_servicediscovery.types.instance_summary

    out: list = []
    for item in value:
        out.append(
            aws_sdk_servicediscovery.types.instance_summary.serialize_aws_json_1_1(item)
        )
    return out


def deserialize_aws_json_1_1(data: list) -> InstanceSummaryList:
    import aws_sdk_servicediscovery.types.instance_summary

    out: InstanceSummaryList = []
    for item in data:
        out.append(
            aws_sdk_servicediscovery.types.instance_summary.deserialize_aws_json_1_1(
                item
            )
        )
    return out
