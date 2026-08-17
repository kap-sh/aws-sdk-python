"""Generated from Smithy shape ``com.amazonaws.dynamodb#DeleteResourcePolicyOutput``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import capo_dynamodb.types.policy_revision_id


class DeleteResourcePolicyOutput(TypedDict, closed=True):
    revision_id: NotRequired["capo_dynamodb.types.policy_revision_id.PolicyRevisionId"]
    """<p>A unique string that represents the revision ID of the policy. If you're comparing revision IDs, make sure to always use string comparison logic.</p> <p>This value will be empty if you make a request against a resource without a policy.</p>"""


# --- awsJson1_0 ser/de ---
def serialize_aws_json_1_0(value: DeleteResourcePolicyOutput) -> dict:
    out: dict = {}
    if "revision_id" in value:
        out["RevisionId"] = value["revision_id"]
    return out


def deserialize_aws_json_1_0(data: dict) -> DeleteResourcePolicyOutput:
    out: DeleteResourcePolicyOutput = {}  # type: ignore[typeddict-item]
    if data.get("RevisionId") is not None:
        out["revision_id"] = data["RevisionId"]
    return out
