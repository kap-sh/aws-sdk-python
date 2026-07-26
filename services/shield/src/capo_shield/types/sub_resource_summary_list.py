"""Generated from Smithy shape ``com.amazonaws.shield#SubResourceSummaryList``."""

from typing import TYPE_CHECKING, TypeAlias

if TYPE_CHECKING:
    import capo_shield.types.sub_resource_summary

SubResourceSummaryList: TypeAlias = list[
    "capo_shield.types.sub_resource_summary.SubResourceSummary"
]


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: SubResourceSummaryList) -> list:
    import capo_shield.types.sub_resource_summary

    out: list = []
    for item in value:
        out.append(capo_shield.types.sub_resource_summary.serialize_aws_json_1_1(item))
    return out


def deserialize_aws_json_1_1(data: list) -> SubResourceSummaryList:
    import capo_shield.types.sub_resource_summary

    out: SubResourceSummaryList = []
    for item in data:
        out.append(
            capo_shield.types.sub_resource_summary.deserialize_aws_json_1_1(item)
        )
    return out
