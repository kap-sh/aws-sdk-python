"""Generated from Smithy shape ``com.amazonaws.opensearchserverless#LifecyclePolicyIdentifier``."""

from typing import TYPE_CHECKING

from typing_extensions import TypedDict

from capo_opensearchserverless.errors import DeserializationError

if TYPE_CHECKING:
    import capo_opensearchserverless.types.lifecycle_policy_type
    import capo_opensearchserverless.types.policy_name


class LifecyclePolicyIdentifier(TypedDict, closed=True):
    type: "capo_opensearchserverless.types.lifecycle_policy_type.LifecyclePolicyType"
    """<p>The type of lifecycle policy.</p>"""
    name: "capo_opensearchserverless.types.policy_name.PolicyName"
    """<p>The name of the lifecycle policy.</p>"""


# --- awsJson1_0 ser/de ---
def serialize_aws_json_1_0(value: LifecyclePolicyIdentifier) -> dict:
    out: dict = {}
    out["type"] = value["type"]
    out["name"] = value["name"]
    return out


def deserialize_aws_json_1_0(data: dict) -> LifecyclePolicyIdentifier:
    out: LifecyclePolicyIdentifier = {}  # type: ignore[typeddict-item]
    if "type" in data:
        out["type"] = data["type"]
    else:
        raise DeserializationError("LifecyclePolicyIdentifier.type required")
    if "name" in data:
        out["name"] = data["name"]
    else:
        raise DeserializationError("LifecyclePolicyIdentifier.name required")
    return out
