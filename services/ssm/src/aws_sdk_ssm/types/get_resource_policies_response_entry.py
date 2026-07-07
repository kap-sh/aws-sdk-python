"""Generated from Smithy shape ``com.amazonaws.ssm#GetResourcePoliciesResponseEntry``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import aws_sdk_ssm.types.policy
    import aws_sdk_ssm.types.policy_hash
    import aws_sdk_ssm.types.policy_id


class GetResourcePoliciesResponseEntry(TypedDict, closed=True):
    policy_id: NotRequired["aws_sdk_ssm.types.policy_id.PolicyId"]
    """<p>A policy ID.</p>"""
    policy_hash: NotRequired["aws_sdk_ssm.types.policy_hash.PolicyHash"]
    """<p>ID of the current policy version. The hash helps to prevent a situation where multiple users attempt to overwrite a policy. You must provide this hash when updating or deleting a policy.</p>"""
    policy: NotRequired["aws_sdk_ssm.types.policy.Policy"]
    """<p>A resource policy helps you to define the IAM entity (for example, an Amazon Web Services account) that can manage your Systems Manager resources. Currently, <code>OpsItemGroup</code> is the only resource that supports Systems Manager resource policies. The resource policy for <code>OpsItemGroup</code> enables Amazon Web Services accounts to view and interact with OpsCenter operational work items (OpsItems).</p>"""


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: GetResourcePoliciesResponseEntry) -> dict:
    out: dict = {}
    if "policy_id" in value:
        out["PolicyId"] = value["policy_id"]
    if "policy_hash" in value:
        out["PolicyHash"] = value["policy_hash"]
    if "policy" in value:
        out["Policy"] = value["policy"]
    return out


def deserialize_aws_json_1_1(data: dict) -> GetResourcePoliciesResponseEntry:
    out: GetResourcePoliciesResponseEntry = {}  # type: ignore[typeddict-item]
    if "PolicyId" in data:
        out["policy_id"] = data["PolicyId"]
    if "PolicyHash" in data:
        out["policy_hash"] = data["PolicyHash"]
    if "Policy" in data:
        out["policy"] = data["Policy"]
    return out
