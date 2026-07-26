"""Generated from Smithy shape ``com.amazonaws.emr#StudioSummaryList``."""

from typing import TYPE_CHECKING, TypeAlias

if TYPE_CHECKING:
    import capo_emr.types.studio_summary

StudioSummaryList: TypeAlias = list["capo_emr.types.studio_summary.StudioSummary"]


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: StudioSummaryList) -> list:
    import capo_emr.types.studio_summary

    out: list = []
    for item in value:
        out.append(capo_emr.types.studio_summary.serialize_aws_json_1_1(item))
    return out


def deserialize_aws_json_1_1(data: list) -> StudioSummaryList:
    import capo_emr.types.studio_summary

    out: StudioSummaryList = []
    for item in data:
        out.append(capo_emr.types.studio_summary.deserialize_aws_json_1_1(item))
    return out
