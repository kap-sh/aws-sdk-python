"""Generated from Smithy shape ``com.amazonaws.resiliencehub#AppSummaryList``."""

from typing import TYPE_CHECKING, TypeAlias

if TYPE_CHECKING:
    import aws_sdk_resiliencehub.types.app_summary

AppSummaryList: TypeAlias = list["aws_sdk_resiliencehub.types.app_summary.AppSummary"]


# --- restJson1 ser/de ---
def serialize_json(value: AppSummaryList) -> list:
    import aws_sdk_resiliencehub.types.app_summary

    out: list = []
    for item in value:
        out.append(aws_sdk_resiliencehub.types.app_summary.serialize_json(item))
    return out


def deserialize_json(data: list) -> AppSummaryList:
    import aws_sdk_resiliencehub.types.app_summary

    out: AppSummaryList = []
    for item in data:
        out.append(aws_sdk_resiliencehub.types.app_summary.deserialize_json(item))
    return out
