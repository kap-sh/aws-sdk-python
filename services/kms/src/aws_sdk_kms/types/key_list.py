"""Generated from Smithy shape ``com.amazonaws.kms#KeyList``."""

from typing import TYPE_CHECKING, TypeAlias

if TYPE_CHECKING:
    import aws_sdk_kms.types.key_list_entry

KeyList: TypeAlias = list["aws_sdk_kms.types.key_list_entry.KeyListEntry"]


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: KeyList) -> list:
    import aws_sdk_kms.types.key_list_entry

    out: list = []
    for item in value:
        out.append(aws_sdk_kms.types.key_list_entry.serialize_aws_json_1_1(item))
    return out


def deserialize_aws_json_1_1(data: list) -> KeyList:
    import aws_sdk_kms.types.key_list_entry

    out: KeyList = []
    for item in data:
        out.append(aws_sdk_kms.types.key_list_entry.deserialize_aws_json_1_1(item))
    return out
