"""Generated from Smithy shape ``com.amazonaws.ssm#OpsItemRelatedItemSummaries``."""

from typing import TYPE_CHECKING, TypeAlias

if TYPE_CHECKING:
    import capo_ssm.types.ops_item_related_item_summary

OpsItemRelatedItemSummaries: TypeAlias = list[
    "capo_ssm.types.ops_item_related_item_summary.OpsItemRelatedItemSummary"
]


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: OpsItemRelatedItemSummaries) -> list:
    import capo_ssm.types.ops_item_related_item_summary

    out: list = []
    for item in value:
        out.append(
            capo_ssm.types.ops_item_related_item_summary.serialize_aws_json_1_1(item)
        )
    return out


def deserialize_aws_json_1_1(data: list) -> OpsItemRelatedItemSummaries:
    import capo_ssm.types.ops_item_related_item_summary

    out: OpsItemRelatedItemSummaries = []
    for item in data:
        out.append(
            capo_ssm.types.ops_item_related_item_summary.deserialize_aws_json_1_1(item)
        )
    return out
