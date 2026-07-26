"""Generated from Smithy shape ``com.amazonaws.lookoutequipment#PutResourcePolicyResponse``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import capo_lookoutequipment.types.policy_revision_id
    import capo_lookoutequipment.types.resource_arn


class PutResourcePolicyResponse(TypedDict, closed=True):
    resource_arn: NotRequired["capo_lookoutequipment.types.resource_arn.ResourceArn"]
    """<p>The Amazon Resource Name (ARN) of the resource for which the policy was created.</p>"""
    policy_revision_id: NotRequired[
        "capo_lookoutequipment.types.policy_revision_id.PolicyRevisionId"
    ]
    """<p>A unique identifier for a revision of the resource policy.</p>"""


# --- awsJson1_0 ser/de ---
def serialize_aws_json_1_0(value: PutResourcePolicyResponse) -> dict:
    out: dict = {}
    if "resource_arn" in value:
        out["ResourceArn"] = value["resource_arn"]
    if "policy_revision_id" in value:
        out["PolicyRevisionId"] = value["policy_revision_id"]
    return out


def deserialize_aws_json_1_0(data: dict) -> PutResourcePolicyResponse:
    out: PutResourcePolicyResponse = {}  # type: ignore[typeddict-item]
    if "ResourceArn" in data:
        out["resource_arn"] = data["ResourceArn"]
    if "PolicyRevisionId" in data:
        out["policy_revision_id"] = data["PolicyRevisionId"]
    return out
