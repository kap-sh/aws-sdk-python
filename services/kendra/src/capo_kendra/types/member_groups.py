"""Generated from Smithy shape ``com.amazonaws.kendra#MemberGroups``."""

from typing import TYPE_CHECKING, TypeAlias

if TYPE_CHECKING:
    import capo_kendra.types.member_group

MemberGroups: TypeAlias = list["capo_kendra.types.member_group.MemberGroup"]


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: MemberGroups) -> list:
    import capo_kendra.types.member_group

    out: list = []
    for item in value:
        out.append(capo_kendra.types.member_group.serialize_aws_json_1_1(item))
    return out


def deserialize_aws_json_1_1(data: list) -> MemberGroups:
    import capo_kendra.types.member_group

    out: MemberGroups = []
    for item in data:
        out.append(capo_kendra.types.member_group.deserialize_aws_json_1_1(item))
    return out
