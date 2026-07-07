"""Generated from Smithy shape ``com.amazonaws.comprehend#PutResourcePolicyResponse``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import aws_sdk_comprehend.types.policy_revision_id


class PutResourcePolicyResponse(TypedDict, closed=True):
    policy_revision_id: NotRequired[
        "aws_sdk_comprehend.types.policy_revision_id.PolicyRevisionId"
    ]
    """<p>The revision ID of the policy. Each time you modify a policy, Amazon Comprehend assigns a new revision ID, and it deletes the prior version of the policy.</p>"""


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: PutResourcePolicyResponse) -> dict:
    out: dict = {}
    if "policy_revision_id" in value:
        out["PolicyRevisionId"] = value["policy_revision_id"]
    return out


def deserialize_aws_json_1_1(data: dict) -> PutResourcePolicyResponse:
    out: PutResourcePolicyResponse = {}  # type: ignore[typeddict-item]
    if "PolicyRevisionId" in data:
        out["policy_revision_id"] = data["PolicyRevisionId"]
    return out
