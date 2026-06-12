"""Generated from Smithy shape ``com.amazonaws.imagebuilder#PutComponentPolicyResponse``."""

from typing import TYPE_CHECKING, TypedDict

from typing_extensions import NotRequired

if TYPE_CHECKING:
    import aws_sdk_imagebuilder.types.component_build_version_arn
    import aws_sdk_imagebuilder.types.non_empty_string


class PutComponentPolicyResponse(TypedDict):
    request_id: NotRequired[
        "aws_sdk_imagebuilder.types.non_empty_string.NonEmptyString"
    ]
    """<p>The request ID that uniquely identifies this request.</p>"""
    component_arn: NotRequired[
        "aws_sdk_imagebuilder.types.component_build_version_arn.ComponentBuildVersionArn"
    ]
    """<p>The Amazon Resource Name (ARN) of the component that this policy was applied to.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: PutComponentPolicyResponse) -> dict:
    out: dict = {}
    if "request_id" in value:
        out["requestId"] = value["request_id"]
    if "component_arn" in value:
        out["componentArn"] = value["component_arn"]
    return out


def deserialize_json(data: dict) -> PutComponentPolicyResponse:
    out: PutComponentPolicyResponse = {}  # type: ignore[typeddict-item]
    if "requestId" in data:
        out["request_id"] = data["requestId"]
    if "componentArn" in data:
        out["component_arn"] = data["componentArn"]
    return out
