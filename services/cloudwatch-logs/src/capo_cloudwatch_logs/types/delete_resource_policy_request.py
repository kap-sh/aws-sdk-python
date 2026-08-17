"""Generated from Smithy shape ``com.amazonaws.cloudwatchlogs#DeleteResourcePolicyRequest``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import capo_cloudwatch_logs.types.arn
    import capo_cloudwatch_logs.types.expected_revision_id
    import capo_cloudwatch_logs.types.policy_name


class DeleteResourcePolicyRequest(TypedDict, closed=True):
    policy_name: NotRequired["capo_cloudwatch_logs.types.policy_name.PolicyName"]
    """<p>The name of the policy to be revoked. This parameter is required.</p>"""
    resource_arn: NotRequired["capo_cloudwatch_logs.types.arn.Arn"]
    """<p>The ARN of the CloudWatch Logs resource for which the resource policy needs to be deleted</p>"""
    expected_revision_id: NotRequired[
        "capo_cloudwatch_logs.types.expected_revision_id.ExpectedRevisionId"
    ]
    """<p>The expected revision ID of the resource policy. Required when deleting a resource-scoped policy to prevent concurrent modifications.</p>"""


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: DeleteResourcePolicyRequest) -> dict:
    out: dict = {}
    if "policy_name" in value:
        out["policyName"] = value["policy_name"]
    if "resource_arn" in value:
        out["resourceArn"] = value["resource_arn"]
    if "expected_revision_id" in value:
        out["expectedRevisionId"] = value["expected_revision_id"]
    return out


def deserialize_aws_json_1_1(data: dict) -> DeleteResourcePolicyRequest:
    out: DeleteResourcePolicyRequest = {}  # type: ignore[typeddict-item]
    if data.get("policyName") is not None:
        out["policy_name"] = data["policyName"]
    if data.get("resourceArn") is not None:
        out["resource_arn"] = data["resourceArn"]
    if data.get("expectedRevisionId") is not None:
        out["expected_revision_id"] = data["expectedRevisionId"]
    return out
