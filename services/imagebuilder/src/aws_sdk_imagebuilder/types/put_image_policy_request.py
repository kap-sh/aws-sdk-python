"""Generated from Smithy shape ``com.amazonaws.imagebuilder#PutImagePolicyRequest``."""

from typing import TYPE_CHECKING

from typing_extensions import TypedDict

from aws_sdk_imagebuilder.errors import DeserializationError

if TYPE_CHECKING:
    import aws_sdk_imagebuilder.types.image_build_version_arn
    import aws_sdk_imagebuilder.types.resource_policy_document


class PutImagePolicyRequest(TypedDict, closed=True):
    image_arn: "aws_sdk_imagebuilder.types.image_build_version_arn.ImageBuildVersionArn"
    """<p>The Amazon Resource Name (ARN) of the image that this policy should be applied to.</p>"""
    policy: "aws_sdk_imagebuilder.types.resource_policy_document.ResourcePolicyDocument"
    """<p>The policy to apply.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: PutImagePolicyRequest) -> dict:
    out: dict = {}
    out["imageArn"] = value["image_arn"]
    out["policy"] = value["policy"]
    return out


def deserialize_json(data: dict) -> PutImagePolicyRequest:
    out: PutImagePolicyRequest = {}  # type: ignore[typeddict-item]
    if "imageArn" in data:
        out["image_arn"] = data["imageArn"]
    else:
        raise DeserializationError("PutImagePolicyRequest.image_arn required")
    if "policy" in data:
        out["policy"] = data["policy"]
    else:
        raise DeserializationError("PutImagePolicyRequest.policy required")
    return out
