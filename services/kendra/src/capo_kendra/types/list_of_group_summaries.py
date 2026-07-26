"""Generated from Smithy shape ``com.amazonaws.kendra#ListOfGroupSummaries``."""

from typing import TYPE_CHECKING, TypeAlias

if TYPE_CHECKING:
    import capo_kendra.types.group_summary

ListOfGroupSummaries: TypeAlias = list["capo_kendra.types.group_summary.GroupSummary"]


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: ListOfGroupSummaries) -> list:
    import capo_kendra.types.group_summary

    out: list = []
    for item in value:
        out.append(capo_kendra.types.group_summary.serialize_aws_json_1_1(item))
    return out


def deserialize_aws_json_1_1(data: list) -> ListOfGroupSummaries:
    import capo_kendra.types.group_summary

    out: ListOfGroupSummaries = []
    for item in data:
        out.append(capo_kendra.types.group_summary.deserialize_aws_json_1_1(item))
    return out
