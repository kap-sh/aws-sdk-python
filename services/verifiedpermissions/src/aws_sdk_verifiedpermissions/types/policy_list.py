"""Generated from Smithy shape ``com.amazonaws.verifiedpermissions#PolicyList``."""

from typing import TYPE_CHECKING, TypeAlias

if TYPE_CHECKING:
    import aws_sdk_verifiedpermissions.types.policy_item

PolicyList: TypeAlias = list["aws_sdk_verifiedpermissions.types.policy_item.PolicyItem"]


# --- awsJson1_0 ser/de ---
def serialize_aws_json_1_0(value: PolicyList) -> list:
    import aws_sdk_verifiedpermissions.types.policy_item

    out: list = []
    for item in value:
        out.append(
            aws_sdk_verifiedpermissions.types.policy_item.serialize_aws_json_1_0(item)
        )
    return out


def deserialize_aws_json_1_0(data: list) -> PolicyList:
    import aws_sdk_verifiedpermissions.types.policy_item

    out: PolicyList = []
    for item in data:
        out.append(
            aws_sdk_verifiedpermissions.types.policy_item.deserialize_aws_json_1_0(item)
        )
    return out
