"""Generated from Smithy shape ``com.amazonaws.opensearchserverless#LifecyclePolicyDetail``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import capo_opensearchserverless.types.lifecycle_policy_type
    import capo_opensearchserverless.types.policy_description
    import capo_opensearchserverless.types.policy_name
    import capo_opensearchserverless.types.policy_version


class LifecyclePolicyDetail(TypedDict, closed=True):
    type: NotRequired[
        "capo_opensearchserverless.types.lifecycle_policy_type.LifecyclePolicyType"
    ]
    """<p>The type of lifecycle policy.</p>"""
    name: NotRequired["capo_opensearchserverless.types.policy_name.PolicyName"]
    """<p>The name of the lifecycle policy.</p>"""
    policy_version: NotRequired[
        "capo_opensearchserverless.types.policy_version.PolicyVersion"
    ]
    """<p>The version of the lifecycle policy.</p>"""
    description: NotRequired[
        "capo_opensearchserverless.types.policy_description.PolicyDescription"
    ]
    """<p>The description of the lifecycle policy.</p>"""
    policy: NotRequired["object"]
    """<p>The JSON policy document without any whitespaces.</p>"""
    created_date: NotRequired["int"]
    """<p>The date the lifecycle policy was created.</p>"""
    last_modified_date: NotRequired["int"]
    """<p>The timestamp of when the lifecycle policy was last modified.</p>"""


# --- awsJson1_0 ser/de ---
def serialize_aws_json_1_0(value: LifecyclePolicyDetail) -> dict:
    out: dict = {}
    if "type" in value:
        out["type"] = value["type"]
    if "name" in value:
        out["name"] = value["name"]
    if "policy_version" in value:
        out["policyVersion"] = value["policy_version"]
    if "description" in value:
        out["description"] = value["description"]
    if "policy" in value:
        out["policy"] = value["policy"]
    if "created_date" in value:
        out["createdDate"] = value["created_date"]
    if "last_modified_date" in value:
        out["lastModifiedDate"] = value["last_modified_date"]
    return out


def deserialize_aws_json_1_0(data: dict) -> LifecyclePolicyDetail:
    out: LifecyclePolicyDetail = {}  # type: ignore[typeddict-item]
    if "type" in data:
        out["type"] = data["type"]
    if "name" in data:
        out["name"] = data["name"]
    if "policyVersion" in data:
        out["policy_version"] = data["policyVersion"]
    if "description" in data:
        out["description"] = data["description"]
    if "policy" in data:
        out["policy"] = data["policy"]
    if "createdDate" in data:
        out["created_date"] = data["createdDate"]
    if "lastModifiedDate" in data:
        out["last_modified_date"] = data["lastModifiedDate"]
    return out
