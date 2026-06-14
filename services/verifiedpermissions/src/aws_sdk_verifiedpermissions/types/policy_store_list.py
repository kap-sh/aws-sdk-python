"""Generated from Smithy shape ``com.amazonaws.verifiedpermissions#PolicyStoreList``."""

from typing import TYPE_CHECKING, TypeAlias

if TYPE_CHECKING:
    import aws_sdk_verifiedpermissions.types.policy_store_item

PolicyStoreList: TypeAlias = list[
    "aws_sdk_verifiedpermissions.types.policy_store_item.PolicyStoreItem"
]


# --- awsJson1_0 ser/de ---
def serialize_aws_json_1_0(value: PolicyStoreList) -> list:
    import aws_sdk_verifiedpermissions.types.policy_store_item

    out: list = []
    for item in value:
        out.append(
            aws_sdk_verifiedpermissions.types.policy_store_item.serialize_aws_json_1_0(
                item
            )
        )
    return out


def deserialize_aws_json_1_0(data: list) -> PolicyStoreList:
    import aws_sdk_verifiedpermissions.types.policy_store_item

    out: PolicyStoreList = []
    for item in data:
        out.append(
            aws_sdk_verifiedpermissions.types.policy_store_item.deserialize_aws_json_1_0(
                item
            )
        )
    return out
