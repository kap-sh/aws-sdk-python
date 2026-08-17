"""Generated from Smithy shape ``com.amazonaws.kms#AliasList``."""

from typing import TYPE_CHECKING, TypeAlias

if TYPE_CHECKING:
    import capo_kms.types.alias_list_entry

AliasList: TypeAlias = list["capo_kms.types.alias_list_entry.AliasListEntry"]


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: AliasList) -> list:
    import capo_kms.types.alias_list_entry

    out: list = []
    for item in value:
        out.append(capo_kms.types.alias_list_entry.serialize_aws_json_1_1(item))
    return out


def deserialize_aws_json_1_1(data: list) -> AliasList:
    import capo_kms.types.alias_list_entry

    out: AliasList = []
    for item in data:
        if item is None:
            continue
        out.append(capo_kms.types.alias_list_entry.deserialize_aws_json_1_1(item))
    return out
