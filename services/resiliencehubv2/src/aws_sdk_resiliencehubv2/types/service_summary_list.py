"""Generated from Smithy shape ``com.amazonaws.resiliencehubv2#ServiceSummaryList``."""

from typing import TYPE_CHECKING, TypeAlias

if TYPE_CHECKING:
    import aws_sdk_resiliencehubv2.types.service_summary

ServiceSummaryList: TypeAlias = list[
    "aws_sdk_resiliencehubv2.types.service_summary.ServiceSummary"
]


# --- restJson1 ser/de ---
def serialize_json(value: ServiceSummaryList) -> list:
    import aws_sdk_resiliencehubv2.types.service_summary

    out: list = []
    for item in value:
        out.append(aws_sdk_resiliencehubv2.types.service_summary.serialize_json(item))
    return out


def deserialize_json(data: list) -> ServiceSummaryList:
    import aws_sdk_resiliencehubv2.types.service_summary

    out: ServiceSummaryList = []
    for item in data:
        out.append(aws_sdk_resiliencehubv2.types.service_summary.deserialize_json(item))
    return out
