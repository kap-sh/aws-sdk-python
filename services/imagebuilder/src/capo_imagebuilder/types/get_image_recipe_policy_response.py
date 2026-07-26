"""Generated from Smithy shape ``com.amazonaws.imagebuilder#GetImageRecipePolicyResponse``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import capo_imagebuilder.types.non_empty_string
    import capo_imagebuilder.types.resource_policy_document


class GetImageRecipePolicyResponse(TypedDict, closed=True):
    request_id: NotRequired["capo_imagebuilder.types.non_empty_string.NonEmptyString"]
    """<p>The request ID that uniquely identifies this request.</p>"""
    policy: NotRequired[
        "capo_imagebuilder.types.resource_policy_document.ResourcePolicyDocument"
    ]
    """<p>The image recipe policy object.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: GetImageRecipePolicyResponse) -> dict:
    out: dict = {}
    if "request_id" in value:
        out["requestId"] = value["request_id"]
    if "policy" in value:
        out["policy"] = value["policy"]
    return out


def deserialize_json(data: dict) -> GetImageRecipePolicyResponse:
    out: GetImageRecipePolicyResponse = {}  # type: ignore[typeddict-item]
    if "requestId" in data:
        out["request_id"] = data["requestId"]
    if "policy" in data:
        out["policy"] = data["policy"]
    return out
