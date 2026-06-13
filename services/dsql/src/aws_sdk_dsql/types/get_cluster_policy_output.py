"""Generated from Smithy shape ``com.amazonaws.dsql#GetClusterPolicyOutput``."""

from typing import TYPE_CHECKING, TypedDict

from aws_sdk_dsql.errors import DeserializationError

if TYPE_CHECKING:
    import aws_sdk_dsql.types.policy_document
    import aws_sdk_dsql.types.policy_version


class GetClusterPolicyOutput(TypedDict):
    policy: "aws_sdk_dsql.types.policy_document.PolicyDocument"
    """<p>The resource-based policy document attached to the cluster, returned as a JSON string.</p>"""
    policy_version: "aws_sdk_dsql.types.policy_version.PolicyVersion"
    """<p>The version of the policy document. This version number is incremented each time the policy is updated.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: GetClusterPolicyOutput) -> dict:
    out: dict = {}
    out["policy"] = value["policy"]
    out["policyVersion"] = value["policy_version"]
    return out


def deserialize_json(data: dict) -> GetClusterPolicyOutput:
    out: GetClusterPolicyOutput = {}  # type: ignore[typeddict-item]
    if "policy" in data:
        out["policy"] = data["policy"]
    else:
        raise DeserializationError("GetClusterPolicyOutput.policy required")
    if "policyVersion" in data:
        out["policy_version"] = data["policyVersion"]
    else:
        raise DeserializationError("GetClusterPolicyOutput.policy_version required")
    return out
