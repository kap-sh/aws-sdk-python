"""Generated from Smithy shape ``com.amazonaws.iotthingsgraph#SystemInstanceSummaries``."""

from typing import TYPE_CHECKING, TypeAlias

if TYPE_CHECKING:
    import aws_sdk_iotthingsgraph.types.system_instance_summary

SystemInstanceSummaries: TypeAlias = list[
    "aws_sdk_iotthingsgraph.types.system_instance_summary.SystemInstanceSummary"
]


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: SystemInstanceSummaries) -> list:
    import aws_sdk_iotthingsgraph.types.system_instance_summary

    out: list = []
    for item in value:
        out.append(
            aws_sdk_iotthingsgraph.types.system_instance_summary.serialize_aws_json_1_1(
                item
            )
        )
    return out


def deserialize_aws_json_1_1(data: list) -> SystemInstanceSummaries:
    import aws_sdk_iotthingsgraph.types.system_instance_summary

    out: SystemInstanceSummaries = []
    for item in data:
        out.append(
            aws_sdk_iotthingsgraph.types.system_instance_summary.deserialize_aws_json_1_1(
                item
            )
        )
    return out
