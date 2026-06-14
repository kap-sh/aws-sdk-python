"""Generated from Smithy shape ``com.amazonaws.verifiedpermissions#DeletePolicyStoreInput``."""

from typing import TYPE_CHECKING, TypedDict

from aws_sdk_verifiedpermissions.errors import DeserializationError

if TYPE_CHECKING:
    import aws_sdk_verifiedpermissions.types.policy_store_id


class DeletePolicyStoreInput(TypedDict):
    policy_store_id: "aws_sdk_verifiedpermissions.types.policy_store_id.PolicyStoreId"
    """<p>Specifies the ID of the policy store that you want to delete.</p> <note> <p>To specify a policy store, the alias name cannot be used. Only the ID can be used.</p> </note>"""


# --- awsJson1_0 ser/de ---
def serialize_aws_json_1_0(value: DeletePolicyStoreInput) -> dict:
    out: dict = {}
    out["policyStoreId"] = value["policy_store_id"]
    return out


def deserialize_aws_json_1_0(data: dict) -> DeletePolicyStoreInput:
    out: DeletePolicyStoreInput = {}  # type: ignore[typeddict-item]
    if "policyStoreId" in data:
        out["policy_store_id"] = data["policyStoreId"]
    else:
        raise DeserializationError("DeletePolicyStoreInput.policy_store_id required")
    return out
