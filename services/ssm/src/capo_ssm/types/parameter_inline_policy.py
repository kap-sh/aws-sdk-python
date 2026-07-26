"""Generated from Smithy shape ``com.amazonaws.ssm#ParameterInlinePolicy``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import capo_ssm.types.string


class ParameterInlinePolicy(TypedDict, closed=True):
    policy_text: NotRequired["capo_ssm.types.string.String"]
    """<p>The JSON text of the policy.</p>"""
    policy_type: NotRequired["capo_ssm.types.string.String"]
    """<p>The type of policy. Parameter Store, a tool in Amazon Web Services Systems Manager, supports the following policy types: Expiration, ExpirationNotification, and NoChangeNotification. </p>"""
    policy_status: NotRequired["capo_ssm.types.string.String"]
    """<p>The status of the policy. Policies report the following statuses: Pending (the policy hasn't been enforced or applied yet), Finished (the policy was applied), Failed (the policy wasn't applied), or InProgress (the policy is being applied now). </p>"""


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: ParameterInlinePolicy) -> dict:
    out: dict = {}
    if "policy_text" in value:
        out["PolicyText"] = value["policy_text"]
    if "policy_type" in value:
        out["PolicyType"] = value["policy_type"]
    if "policy_status" in value:
        out["PolicyStatus"] = value["policy_status"]
    return out


def deserialize_aws_json_1_1(data: dict) -> ParameterInlinePolicy:
    out: ParameterInlinePolicy = {}  # type: ignore[typeddict-item]
    if "PolicyText" in data:
        out["policy_text"] = data["PolicyText"]
    if "PolicyType" in data:
        out["policy_type"] = data["PolicyType"]
    if "PolicyStatus" in data:
        out["policy_status"] = data["PolicyStatus"]
    return out
