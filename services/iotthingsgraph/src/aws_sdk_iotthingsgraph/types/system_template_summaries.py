"""Generated from Smithy shape ``com.amazonaws.iotthingsgraph#SystemTemplateSummaries``."""

from typing import TYPE_CHECKING, TypeAlias

if TYPE_CHECKING:
    import aws_sdk_iotthingsgraph.types.system_template_summary

SystemTemplateSummaries: TypeAlias = list[
    "aws_sdk_iotthingsgraph.types.system_template_summary.SystemTemplateSummary"
]


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: SystemTemplateSummaries) -> list:
    import aws_sdk_iotthingsgraph.types.system_template_summary

    out: list = []
    for item in value:
        out.append(
            aws_sdk_iotthingsgraph.types.system_template_summary.serialize_aws_json_1_1(
                item
            )
        )
    return out


def deserialize_aws_json_1_1(data: list) -> SystemTemplateSummaries:
    import aws_sdk_iotthingsgraph.types.system_template_summary

    out: SystemTemplateSummaries = []
    for item in data:
        out.append(
            aws_sdk_iotthingsgraph.types.system_template_summary.deserialize_aws_json_1_1(
                item
            )
        )
    return out
