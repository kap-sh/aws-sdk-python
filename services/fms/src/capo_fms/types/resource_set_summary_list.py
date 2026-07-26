"""Generated from Smithy shape ``com.amazonaws.fms#ResourceSetSummaryList``."""

from typing import TYPE_CHECKING, TypeAlias

if TYPE_CHECKING:
    import capo_fms.types.resource_set_summary

ResourceSetSummaryList: TypeAlias = list[
    "capo_fms.types.resource_set_summary.ResourceSetSummary"
]


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: ResourceSetSummaryList) -> list:
    import capo_fms.types.resource_set_summary

    out: list = []
    for item in value:
        out.append(capo_fms.types.resource_set_summary.serialize_aws_json_1_1(item))
    return out


def deserialize_aws_json_1_1(data: list) -> ResourceSetSummaryList:
    import capo_fms.types.resource_set_summary

    out: ResourceSetSummaryList = []
    for item in data:
        out.append(capo_fms.types.resource_set_summary.deserialize_aws_json_1_1(item))
    return out
