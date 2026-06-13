"""Generated from Smithy shape ``com.amazonaws.bedrock#GetResourcePolicyResponse``."""

from typing import TYPE_CHECKING, TypedDict

from typing_extensions import NotRequired

if TYPE_CHECKING:
    import aws_sdk_bedrock.types.resource_policy_document


class GetResourcePolicyResponse(TypedDict):
    resource_policy: NotRequired[
        "aws_sdk_bedrock.types.resource_policy_document.ResourcePolicyDocument"
    ]
    """<p>The JSON string representing the Bedrock resource policy.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: GetResourcePolicyResponse) -> dict:
    out: dict = {}
    if "resource_policy" in value:
        out["resourcePolicy"] = value["resource_policy"]
    return out


def deserialize_json(data: dict) -> GetResourcePolicyResponse:
    out: GetResourcePolicyResponse = {}  # type: ignore[typeddict-item]
    if "resourcePolicy" in data:
        out["resource_policy"] = data["resourcePolicy"]
    return out
