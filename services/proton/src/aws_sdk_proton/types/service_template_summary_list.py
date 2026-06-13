"""Generated from Smithy shape ``com.amazonaws.proton#ServiceTemplateSummaryList``."""

from typing import TYPE_CHECKING, TypeAlias

if TYPE_CHECKING:
    import aws_sdk_proton.types.service_template_summary

ServiceTemplateSummaryList: TypeAlias = list[
    "aws_sdk_proton.types.service_template_summary.ServiceTemplateSummary"
]


# --- awsJson1_0 ser/de ---
def serialize_aws_json_1_0(value: ServiceTemplateSummaryList) -> list:
    import aws_sdk_proton.types.service_template_summary

    out: list = []
    for item in value:
        out.append(
            aws_sdk_proton.types.service_template_summary.serialize_aws_json_1_0(item)
        )
    return out


def deserialize_aws_json_1_0(data: list) -> ServiceTemplateSummaryList:
    import aws_sdk_proton.types.service_template_summary

    out: ServiceTemplateSummaryList = []
    for item in data:
        out.append(
            aws_sdk_proton.types.service_template_summary.deserialize_aws_json_1_0(item)
        )
    return out
