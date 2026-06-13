"""Generated from Smithy shape ``com.amazonaws.proton#ServiceTemplateVersionSummaryList``."""

from typing import TYPE_CHECKING, TypeAlias

if TYPE_CHECKING:
    import aws_sdk_proton.types.service_template_version_summary

ServiceTemplateVersionSummaryList: TypeAlias = list[
    "aws_sdk_proton.types.service_template_version_summary.ServiceTemplateVersionSummary"
]


# --- awsJson1_0 ser/de ---
def serialize_aws_json_1_0(value: ServiceTemplateVersionSummaryList) -> list:
    import aws_sdk_proton.types.service_template_version_summary

    out: list = []
    for item in value:
        out.append(
            aws_sdk_proton.types.service_template_version_summary.serialize_aws_json_1_0(
                item
            )
        )
    return out


def deserialize_aws_json_1_0(data: list) -> ServiceTemplateVersionSummaryList:
    import aws_sdk_proton.types.service_template_version_summary

    out: ServiceTemplateVersionSummaryList = []
    for item in data:
        out.append(
            aws_sdk_proton.types.service_template_version_summary.deserialize_aws_json_1_0(
                item
            )
        )
    return out
