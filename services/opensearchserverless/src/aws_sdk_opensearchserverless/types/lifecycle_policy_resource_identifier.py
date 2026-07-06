"""Generated from Smithy shape ``com.amazonaws.opensearchserverless#LifecyclePolicyResourceIdentifier``."""

from typing import TYPE_CHECKING

from typing_extensions import TypedDict

from aws_sdk_opensearchserverless.errors import DeserializationError

if TYPE_CHECKING:
    import aws_sdk_opensearchserverless.types.lifecycle_policy_type
    import aws_sdk_opensearchserverless.types.resource_name


class LifecyclePolicyResourceIdentifier(TypedDict, closed=True):
    type: "aws_sdk_opensearchserverless.types.lifecycle_policy_type.LifecyclePolicyType"
    """<p>The type of lifecycle policy.</p>"""
    resource: "aws_sdk_opensearchserverless.types.resource_name.ResourceName"
    """<p>The name of the OpenSearch Serverless ilndex resource.</p>"""


# --- awsJson1_0 ser/de ---
def serialize_aws_json_1_0(value: LifecyclePolicyResourceIdentifier) -> dict:
    out: dict = {}
    out["type"] = value["type"]
    out["resource"] = value["resource"]
    return out


def deserialize_aws_json_1_0(data: dict) -> LifecyclePolicyResourceIdentifier:
    out: LifecyclePolicyResourceIdentifier = {}  # type: ignore[typeddict-item]
    if "type" in data:
        out["type"] = data["type"]
    else:
        raise DeserializationError("LifecyclePolicyResourceIdentifier.type required")
    if "resource" in data:
        out["resource"] = data["resource"]
    else:
        raise DeserializationError(
            "LifecyclePolicyResourceIdentifier.resource required"
        )
    return out
