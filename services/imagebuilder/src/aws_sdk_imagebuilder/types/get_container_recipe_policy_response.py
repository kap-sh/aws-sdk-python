"""Generated from Smithy shape ``com.amazonaws.imagebuilder#GetContainerRecipePolicyResponse``."""

from typing import TYPE_CHECKING, TypedDict

from typing_extensions import NotRequired

if TYPE_CHECKING:
    import aws_sdk_imagebuilder.types.non_empty_string
    import aws_sdk_imagebuilder.types.resource_policy_document


class GetContainerRecipePolicyResponse(TypedDict):
    request_id: NotRequired[
        "aws_sdk_imagebuilder.types.non_empty_string.NonEmptyString"
    ]
    """<p>The request ID that uniquely identifies this request.</p>"""
    policy: NotRequired[
        "aws_sdk_imagebuilder.types.resource_policy_document.ResourcePolicyDocument"
    ]
    """<p>The container recipe policy object that is returned.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: GetContainerRecipePolicyResponse) -> dict:
    out: dict = {}
    if "request_id" in value:
        out["requestId"] = value["request_id"]
    if "policy" in value:
        out["policy"] = value["policy"]
    return out


def deserialize_json(data: dict) -> GetContainerRecipePolicyResponse:
    out: GetContainerRecipePolicyResponse = {}  # type: ignore[typeddict-item]
    if "requestId" in data:
        out["request_id"] = data["requestId"]
    if "policy" in data:
        out["policy"] = data["policy"]
    return out
