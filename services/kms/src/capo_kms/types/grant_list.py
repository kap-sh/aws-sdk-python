"""Generated from Smithy shape ``com.amazonaws.kms#GrantList``."""

from typing import TYPE_CHECKING, TypeAlias

if TYPE_CHECKING:
    import capo_kms.types.grant_list_entry

GrantList: TypeAlias = list["capo_kms.types.grant_list_entry.GrantListEntry"]


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: GrantList) -> list:
    import capo_kms.types.grant_list_entry

    out: list = []
    for item in value:
        out.append(capo_kms.types.grant_list_entry.serialize_aws_json_1_1(item))
    return out


def deserialize_aws_json_1_1(data: list) -> GrantList:
    import capo_kms.types.grant_list_entry

    out: GrantList = []
    for item in data:
        if item is None:
            continue
        out.append(capo_kms.types.grant_list_entry.deserialize_aws_json_1_1(item))
    return out
