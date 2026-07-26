"""Generated from Smithy shape ``com.amazonaws.comprehend#DeleteResourcePolicyRequest``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

from capo_comprehend.errors import DeserializationError

if TYPE_CHECKING:
    import capo_comprehend.types.comprehend_model_arn
    import capo_comprehend.types.policy_revision_id


class DeleteResourcePolicyRequest(TypedDict, closed=True):
    resource_arn: "capo_comprehend.types.comprehend_model_arn.ComprehendModelArn"
    """<p>The Amazon Resource Name (ARN) of the custom model version that has the policy to delete.</p>"""
    policy_revision_id: NotRequired[
        "capo_comprehend.types.policy_revision_id.PolicyRevisionId"
    ]
    """<p>The revision ID of the policy to delete.</p>"""


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: DeleteResourcePolicyRequest) -> dict:
    out: dict = {}
    out["ResourceArn"] = value["resource_arn"]
    if "policy_revision_id" in value:
        out["PolicyRevisionId"] = value["policy_revision_id"]
    return out


def deserialize_aws_json_1_1(data: dict) -> DeleteResourcePolicyRequest:
    out: DeleteResourcePolicyRequest = {}  # type: ignore[typeddict-item]
    if "ResourceArn" in data:
        out["resource_arn"] = data["ResourceArn"]
    else:
        raise DeserializationError("DeleteResourcePolicyRequest.resource_arn required")
    if "PolicyRevisionId" in data:
        out["policy_revision_id"] = data["PolicyRevisionId"]
    return out
