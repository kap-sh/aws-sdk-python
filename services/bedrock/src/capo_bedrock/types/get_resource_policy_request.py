"""Generated from Smithy shape ``com.amazonaws.bedrock#GetResourcePolicyRequest``."""

from typing import TYPE_CHECKING

from typing_extensions import TypedDict

if TYPE_CHECKING:
    import capo_bedrock.types.resource_policy_resource_arn


class GetResourcePolicyRequest(TypedDict, closed=True):
    resource_arn: (
        "capo_bedrock.types.resource_policy_resource_arn.ResourcePolicyResourceArn"
    )
    """<p>The ARN of the Bedrock resource to which this resource policy applies.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: GetResourcePolicyRequest) -> dict:
    out: dict = {}
    return out


def deserialize_json(data: dict) -> GetResourcePolicyRequest:
    out: GetResourcePolicyRequest = {}  # type: ignore[typeddict-item]
    return out
