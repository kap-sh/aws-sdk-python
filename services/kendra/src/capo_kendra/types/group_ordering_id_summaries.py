"""Generated from Smithy shape ``com.amazonaws.kendra#GroupOrderingIdSummaries``."""

from typing import TYPE_CHECKING, TypeAlias

if TYPE_CHECKING:
    import capo_kendra.types.group_ordering_id_summary

GroupOrderingIdSummaries: TypeAlias = list[
    "capo_kendra.types.group_ordering_id_summary.GroupOrderingIdSummary"
]


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: GroupOrderingIdSummaries) -> list:
    import capo_kendra.types.group_ordering_id_summary

    out: list = []
    for item in value:
        out.append(
            capo_kendra.types.group_ordering_id_summary.serialize_aws_json_1_1(item)
        )
    return out


def deserialize_aws_json_1_1(data: list) -> GroupOrderingIdSummaries:
    import capo_kendra.types.group_ordering_id_summary

    out: GroupOrderingIdSummaries = []
    for item in data:
        out.append(
            capo_kendra.types.group_ordering_id_summary.deserialize_aws_json_1_1(item)
        )
    return out
