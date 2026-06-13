"""Generated from Smithy shape ``com.amazonaws.resiliencehubv2#SystemSummaryList``."""

from typing import TYPE_CHECKING, TypeAlias

if TYPE_CHECKING:
    import aws_sdk_resiliencehubv2.types.system_summary

SystemSummaryList: TypeAlias = list[
    "aws_sdk_resiliencehubv2.types.system_summary.SystemSummary"
]


# --- restJson1 ser/de ---
def serialize_json(value: SystemSummaryList) -> list:
    import aws_sdk_resiliencehubv2.types.system_summary

    out: list = []
    for item in value:
        out.append(aws_sdk_resiliencehubv2.types.system_summary.serialize_json(item))
    return out


def deserialize_json(data: list) -> SystemSummaryList:
    import aws_sdk_resiliencehubv2.types.system_summary

    out: SystemSummaryList = []
    for item in data:
        out.append(aws_sdk_resiliencehubv2.types.system_summary.deserialize_json(item))
    return out
