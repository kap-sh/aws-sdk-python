"""Generated from Smithy shape ``com.amazonaws.bedrock#PutResourcePolicyResponse``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import capo_bedrock.types.resource_policy_resource_arn


class PutResourcePolicyResponse(TypedDict, closed=True):
    resource_arn: NotRequired[
        "capo_bedrock.types.resource_policy_resource_arn.ResourcePolicyResourceArn"
    ]
    """<p>The ARN of the Bedrock resource to which this resource policy applies.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: PutResourcePolicyResponse) -> dict:
    out: dict = {}
    if "resource_arn" in value:
        out["resourceArn"] = value["resource_arn"]
    return out


def deserialize_json(data: dict) -> PutResourcePolicyResponse:
    out: PutResourcePolicyResponse = {}  # type: ignore[typeddict-item]
    if data.get("resourceArn") is not None:
        out["resource_arn"] = data["resourceArn"]
    return out
