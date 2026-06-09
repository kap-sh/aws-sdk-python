"""Generated from Smithy shape ``com.amazonaws.kms#GrantList``."""

from typing import TYPE_CHECKING, TypeAlias

if TYPE_CHECKING:
    import aws_sdk_kms.types.grant_list_entry

GrantList: TypeAlias = list["aws_sdk_kms.types.grant_list_entry.GrantListEntry"]


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: GrantList) -> list:
    import aws_sdk_kms.types.grant_list_entry

    out: list = []
    for item in value:
        out.append(aws_sdk_kms.types.grant_list_entry.serialize_aws_json_1_1(item))
    return out


def deserialize_aws_json_1_1(data: list) -> GrantList:
    import aws_sdk_kms.types.grant_list_entry

    out: GrantList = []
    for item in data:
        out.append(aws_sdk_kms.types.grant_list_entry.deserialize_aws_json_1_1(item))
    return out
