"""Generated from Smithy shape ``com.amazonaws.opensearchserverless#LifecyclePolicySummary``."""

from typing import TYPE_CHECKING, TypedDict

from typing_extensions import NotRequired

if TYPE_CHECKING:
    import aws_sdk_opensearchserverless.types.lifecycle_policy_type
    import aws_sdk_opensearchserverless.types.policy_description
    import aws_sdk_opensearchserverless.types.policy_name
    import aws_sdk_opensearchserverless.types.policy_version


class LifecyclePolicySummary(TypedDict):
    type: NotRequired[
        "aws_sdk_opensearchserverless.types.lifecycle_policy_type.LifecyclePolicyType"
    ]
    """<p>The type of lifecycle policy.</p>"""
    name: NotRequired["aws_sdk_opensearchserverless.types.policy_name.PolicyName"]
    """<p>The name of the lifecycle policy.</p>"""
    policy_version: NotRequired[
        "aws_sdk_opensearchserverless.types.policy_version.PolicyVersion"
    ]
    """<p>The version of the lifecycle policy.</p>"""
    description: NotRequired[
        "aws_sdk_opensearchserverless.types.policy_description.PolicyDescription"
    ]
    """<p>The description of the lifecycle policy.</p>"""
    created_date: NotRequired["int"]
    """<p>The Epoch time when the lifecycle policy was created.</p>"""
    last_modified_date: NotRequired["int"]
    """<p>The date and time when the lifecycle policy was last modified.</p>"""


# --- awsJson1_0 ser/de ---
def serialize_aws_json_1_0(value: LifecyclePolicySummary) -> dict:
    out: dict = {}
    if "type" in value:
        out["type"] = value["type"]
    if "name" in value:
        out["name"] = value["name"]
    if "policy_version" in value:
        out["policyVersion"] = value["policy_version"]
    if "description" in value:
        out["description"] = value["description"]
    if "created_date" in value:
        out["createdDate"] = value["created_date"]
    if "last_modified_date" in value:
        out["lastModifiedDate"] = value["last_modified_date"]
    return out


def deserialize_aws_json_1_0(data: dict) -> LifecyclePolicySummary:
    out: LifecyclePolicySummary = {}  # type: ignore[typeddict-item]
    if "type" in data:
        out["type"] = data["type"]
    if "name" in data:
        out["name"] = data["name"]
    if "policyVersion" in data:
        out["policy_version"] = data["policyVersion"]
    if "description" in data:
        out["description"] = data["description"]
    if "createdDate" in data:
        out["created_date"] = data["createdDate"]
    if "lastModifiedDate" in data:
        out["last_modified_date"] = data["lastModifiedDate"]
    return out
