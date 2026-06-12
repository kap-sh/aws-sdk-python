"""Generated from Smithy shape ``com.amazonaws.apprunner#ServiceSummaryList``."""

from typing import TYPE_CHECKING, TypeAlias

if TYPE_CHECKING:
    import aws_sdk_apprunner.types.service_summary

ServiceSummaryList: TypeAlias = list[
    "aws_sdk_apprunner.types.service_summary.ServiceSummary"
]


# --- awsJson1_0 ser/de ---
def serialize_aws_json_1_0(value: ServiceSummaryList) -> list:
    import aws_sdk_apprunner.types.service_summary

    out: list = []
    for item in value:
        out.append(aws_sdk_apprunner.types.service_summary.serialize_aws_json_1_0(item))
    return out


def deserialize_aws_json_1_0(data: list) -> ServiceSummaryList:
    import aws_sdk_apprunner.types.service_summary

    out: ServiceSummaryList = []
    for item in data:
        out.append(
            aws_sdk_apprunner.types.service_summary.deserialize_aws_json_1_0(item)
        )
    return out
