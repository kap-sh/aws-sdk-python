"""Generated from Smithy shape ``com.amazonaws.securityhub#AwsIamAttachedManagedPolicy``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import capo_securityhub.types.non_empty_string


class AwsIamAttachedManagedPolicy(TypedDict, closed=True):
    policy_name: NotRequired["capo_securityhub.types.non_empty_string.NonEmptyString"]
    """<p>The name of the policy.</p>"""
    policy_arn: NotRequired["capo_securityhub.types.non_empty_string.NonEmptyString"]
    """<p>The ARN of the policy.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: AwsIamAttachedManagedPolicy) -> dict:
    out: dict = {}
    if "policy_name" in value:
        out["PolicyName"] = value["policy_name"]
    if "policy_arn" in value:
        out["PolicyArn"] = value["policy_arn"]
    return out


def deserialize_json(data: dict) -> AwsIamAttachedManagedPolicy:
    out: AwsIamAttachedManagedPolicy = {}  # type: ignore[typeddict-item]
    if "PolicyName" in data:
        out["policy_name"] = data["PolicyName"]
    if "PolicyArn" in data:
        out["policy_arn"] = data["PolicyArn"]
    return out
