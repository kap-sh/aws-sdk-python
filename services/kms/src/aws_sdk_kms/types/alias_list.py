"""Generated from Smithy shape ``com.amazonaws.kms#AliasList``."""

from typing import TYPE_CHECKING, TypeAlias

if TYPE_CHECKING:
    import aws_sdk_kms.types.alias_list_entry

AliasList: TypeAlias = list["aws_sdk_kms.types.alias_list_entry.AliasListEntry"]


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: AliasList) -> list:
    import aws_sdk_kms.types.alias_list_entry

    out: list = []
    for item in value:
        out.append(aws_sdk_kms.types.alias_list_entry.serialize_aws_json_1_1(item))
    return out


def deserialize_aws_json_1_1(data: list) -> AliasList:
    import aws_sdk_kms.types.alias_list_entry

    out: AliasList = []
    for item in data:
        out.append(aws_sdk_kms.types.alias_list_entry.deserialize_aws_json_1_1(item))
    return out
