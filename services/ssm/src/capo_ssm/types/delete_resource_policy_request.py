"""Generated from Smithy shape ``com.amazonaws.ssm#DeleteResourcePolicyRequest``."""

from typing import TYPE_CHECKING

from typing_extensions import TypedDict

from capo_ssm.errors import DeserializationError

if TYPE_CHECKING:
    import capo_ssm.types.policy_hash
    import capo_ssm.types.policy_id
    import capo_ssm.types.resource_arn_string


class DeleteResourcePolicyRequest(TypedDict, closed=True):
    resource_arn: "capo_ssm.types.resource_arn_string.ResourceArnString"
    """<p>Amazon Resource Name (ARN) of the resource to which the policies are attached.</p>"""
    policy_id: "capo_ssm.types.policy_id.PolicyId"
    """<p>The policy ID.</p>"""
    policy_hash: "capo_ssm.types.policy_hash.PolicyHash"
    """<p>ID of the current policy version. The hash helps to prevent multiple calls from attempting to overwrite a policy.</p>"""


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: DeleteResourcePolicyRequest) -> dict:
    out: dict = {}
    out["ResourceArn"] = value["resource_arn"]
    out["PolicyId"] = value["policy_id"]
    out["PolicyHash"] = value["policy_hash"]
    return out


def deserialize_aws_json_1_1(data: dict) -> DeleteResourcePolicyRequest:
    out: DeleteResourcePolicyRequest = {}  # type: ignore[typeddict-item]
    if data.get("ResourceArn") is not None:
        out["resource_arn"] = data["ResourceArn"]
    else:
        raise DeserializationError("DeleteResourcePolicyRequest.resource_arn required")
    if data.get("PolicyId") is not None:
        out["policy_id"] = data["PolicyId"]
    else:
        raise DeserializationError("DeleteResourcePolicyRequest.policy_id required")
    if data.get("PolicyHash") is not None:
        out["policy_hash"] = data["PolicyHash"]
    else:
        raise DeserializationError("DeleteResourcePolicyRequest.policy_hash required")
    return out
