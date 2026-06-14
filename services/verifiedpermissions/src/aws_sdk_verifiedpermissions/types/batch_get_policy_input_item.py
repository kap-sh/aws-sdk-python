"""Generated from Smithy shape ``com.amazonaws.verifiedpermissions#BatchGetPolicyInputItem``."""

from typing import TYPE_CHECKING, TypedDict

from aws_sdk_verifiedpermissions.errors import DeserializationError

if TYPE_CHECKING:
    import aws_sdk_verifiedpermissions.types.policy_id
    import aws_sdk_verifiedpermissions.types.policy_store_id


class BatchGetPolicyInputItem(TypedDict):
    policy_store_id: "aws_sdk_verifiedpermissions.types.policy_store_id.PolicyStoreId"
    """<p>The identifier of the policy store where the policy you want information about is stored.</p>"""
    policy_id: "aws_sdk_verifiedpermissions.types.policy_id.PolicyId"
    """<p>The identifier of the policy you want information about.</p> <p>You can use the policy name in place of the policy ID. When using a name, prefix it with <code>name/</code>. For example:</p> <ul> <li> <p>ID: <code>SPEXAMPLEabcdefg111111</code> </p> </li> <li> <p>Name: <code>name/example-policy</code> </p> </li> </ul>"""


# --- awsJson1_0 ser/de ---
def serialize_aws_json_1_0(value: BatchGetPolicyInputItem) -> dict:
    out: dict = {}
    out["policyStoreId"] = value["policy_store_id"]
    out["policyId"] = value["policy_id"]
    return out


def deserialize_aws_json_1_0(data: dict) -> BatchGetPolicyInputItem:
    out: BatchGetPolicyInputItem = {}  # type: ignore[typeddict-item]
    if "policyStoreId" in data:
        out["policy_store_id"] = data["policyStoreId"]
    else:
        raise DeserializationError("BatchGetPolicyInputItem.policy_store_id required")
    if "policyId" in data:
        out["policy_id"] = data["policyId"]
    else:
        raise DeserializationError("BatchGetPolicyInputItem.policy_id required")
    return out
