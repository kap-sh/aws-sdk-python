"""Generated from Smithy shape ``com.amazonaws.kendra#IssueSubEntityFilter``."""

from typing import TYPE_CHECKING, TypeAlias

if TYPE_CHECKING:
    import capo_kendra.types.issue_sub_entity

IssueSubEntityFilter: TypeAlias = list[
    "capo_kendra.types.issue_sub_entity.IssueSubEntity"
]


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: IssueSubEntityFilter) -> list:
    import capo_kendra.types.issue_sub_entity

    out: list = []
    for item in value:
        out.append(capo_kendra.types.issue_sub_entity.serialize_aws_json_1_1(item))
    return out


def deserialize_aws_json_1_1(data: list) -> IssueSubEntityFilter:
    import capo_kendra.types.issue_sub_entity

    out: IssueSubEntityFilter = []
    for item in data:
        out.append(capo_kendra.types.issue_sub_entity.deserialize_aws_json_1_1(item))
    return out
