"""Generated from Smithy shape ``com.amazonaws.proton#EnvironmentTemplateSummaryList``."""

from typing import TYPE_CHECKING, TypeAlias

if TYPE_CHECKING:
    import aws_sdk_proton.types.environment_template_summary

EnvironmentTemplateSummaryList: TypeAlias = list[
    "aws_sdk_proton.types.environment_template_summary.EnvironmentTemplateSummary"
]


# --- awsJson1_0 ser/de ---
def serialize_aws_json_1_0(value: EnvironmentTemplateSummaryList) -> list:
    import aws_sdk_proton.types.environment_template_summary

    out: list = []
    for item in value:
        out.append(
            aws_sdk_proton.types.environment_template_summary.serialize_aws_json_1_0(
                item
            )
        )
    return out


def deserialize_aws_json_1_0(data: list) -> EnvironmentTemplateSummaryList:
    import aws_sdk_proton.types.environment_template_summary

    out: EnvironmentTemplateSummaryList = []
    for item in data:
        out.append(
            aws_sdk_proton.types.environment_template_summary.deserialize_aws_json_1_0(
                item
            )
        )
    return out
