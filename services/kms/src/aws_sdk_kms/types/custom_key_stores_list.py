"""Generated from Smithy shape ``com.amazonaws.kms#CustomKeyStoresList``."""

from typing import TYPE_CHECKING, TypeAlias

if TYPE_CHECKING:
    import aws_sdk_kms.types.custom_key_stores_list_entry

CustomKeyStoresList: TypeAlias = list[
    "aws_sdk_kms.types.custom_key_stores_list_entry.CustomKeyStoresListEntry"
]


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: CustomKeyStoresList) -> list:
    import aws_sdk_kms.types.custom_key_stores_list_entry

    out: list = []
    for item in value:
        out.append(
            aws_sdk_kms.types.custom_key_stores_list_entry.serialize_aws_json_1_1(item)
        )
    return out


def deserialize_aws_json_1_1(data: list) -> CustomKeyStoresList:
    import aws_sdk_kms.types.custom_key_stores_list_entry

    out: CustomKeyStoresList = []
    for item in data:
        out.append(
            aws_sdk_kms.types.custom_key_stores_list_entry.deserialize_aws_json_1_1(
                item
            )
        )
    return out
