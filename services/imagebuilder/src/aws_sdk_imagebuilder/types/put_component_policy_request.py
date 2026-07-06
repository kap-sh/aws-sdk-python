"""Generated from Smithy shape ``com.amazonaws.imagebuilder#PutComponentPolicyRequest``."""

from typing import TYPE_CHECKING

from typing_extensions import TypedDict

from aws_sdk_imagebuilder.errors import DeserializationError

if TYPE_CHECKING:
    import aws_sdk_imagebuilder.types.component_build_version_arn
    import aws_sdk_imagebuilder.types.resource_policy_document


class PutComponentPolicyRequest(TypedDict, closed=True):
    component_arn: "aws_sdk_imagebuilder.types.component_build_version_arn.ComponentBuildVersionArn"
    """<p>The Amazon Resource Name (ARN) of the component that this policy should be applied to.</p>"""
    policy: "aws_sdk_imagebuilder.types.resource_policy_document.ResourcePolicyDocument"
    """<p>The policy to apply.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: PutComponentPolicyRequest) -> dict:
    out: dict = {}
    out["componentArn"] = value["component_arn"]
    out["policy"] = value["policy"]
    return out


def deserialize_json(data: dict) -> PutComponentPolicyRequest:
    out: PutComponentPolicyRequest = {}  # type: ignore[typeddict-item]
    if "componentArn" in data:
        out["component_arn"] = data["componentArn"]
    else:
        raise DeserializationError("PutComponentPolicyRequest.component_arn required")
    if "policy" in data:
        out["policy"] = data["policy"]
    else:
        raise DeserializationError("PutComponentPolicyRequest.policy required")
    return out
