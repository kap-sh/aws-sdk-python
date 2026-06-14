"""Generated from Smithy shape ``com.amazonaws.verifiedpermissions#PolicyStoreAliasList``."""

from typing import TYPE_CHECKING, TypeAlias

if TYPE_CHECKING:
    import aws_sdk_verifiedpermissions.types.policy_store_alias_item

PolicyStoreAliasList: TypeAlias = list[
    "aws_sdk_verifiedpermissions.types.policy_store_alias_item.PolicyStoreAliasItem"
]


# --- awsJson1_0 ser/de ---
def serialize_aws_json_1_0(value: PolicyStoreAliasList) -> list:
    import aws_sdk_verifiedpermissions.types.policy_store_alias_item

    out: list = []
    for item in value:
        out.append(
            aws_sdk_verifiedpermissions.types.policy_store_alias_item.serialize_aws_json_1_0(
                item
            )
        )
    return out


def deserialize_aws_json_1_0(data: list) -> PolicyStoreAliasList:
    import aws_sdk_verifiedpermissions.types.policy_store_alias_item

    out: PolicyStoreAliasList = []
    for item in data:
        out.append(
            aws_sdk_verifiedpermissions.types.policy_store_alias_item.deserialize_aws_json_1_0(
                item
            )
        )
    return out
