"""Generated from Smithy shape ``com.amazonaws.verifiedpermissions#BatchGetPolicyErrorItem``."""

from typing import TYPE_CHECKING, TypedDict

from aws_sdk_verifiedpermissions.errors import DeserializationError

if TYPE_CHECKING:
    import aws_sdk_verifiedpermissions.types.batch_get_policy_error_code


class BatchGetPolicyErrorItem(TypedDict):
    code: "aws_sdk_verifiedpermissions.types.batch_get_policy_error_code.BatchGetPolicyErrorCode"
    """<p>The error code that was returned.</p>"""
    policy_store_id: "str"
    """<p>The identifier of the policy store associated with the failed request.</p>"""
    policy_id: "str"
    """<p>The identifier of the policy associated with the failed request.</p>"""
    message: "str"
    """<p>A detailed error message.</p>"""


# --- awsJson1_0 ser/de ---
def serialize_aws_json_1_0(value: BatchGetPolicyErrorItem) -> dict:
    out: dict = {}
    import aws_sdk_verifiedpermissions.types.batch_get_policy_error_code

    out["code"] = (
        aws_sdk_verifiedpermissions.types.batch_get_policy_error_code.serialize_aws_json_1_0(
            value["code"]
        )
    )
    out["policyStoreId"] = value["policy_store_id"]
    out["policyId"] = value["policy_id"]
    out["message"] = value["message"]
    return out


def deserialize_aws_json_1_0(data: dict) -> BatchGetPolicyErrorItem:
    out: BatchGetPolicyErrorItem = {}  # type: ignore[typeddict-item]
    if "code" in data:
        import aws_sdk_verifiedpermissions.types.batch_get_policy_error_code

        out["code"] = (
            aws_sdk_verifiedpermissions.types.batch_get_policy_error_code.deserialize_aws_json_1_0(
                data["code"]
            )
        )
    else:
        raise DeserializationError("BatchGetPolicyErrorItem.code required")
    if "policyStoreId" in data:
        out["policy_store_id"] = data["policyStoreId"]
    else:
        raise DeserializationError("BatchGetPolicyErrorItem.policy_store_id required")
    if "policyId" in data:
        out["policy_id"] = data["policyId"]
    else:
        raise DeserializationError("BatchGetPolicyErrorItem.policy_id required")
    if "message" in data:
        out["message"] = data["message"]
    else:
        raise DeserializationError("BatchGetPolicyErrorItem.message required")
    return out
