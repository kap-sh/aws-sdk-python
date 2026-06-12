"""Generated from Smithy shape ``com.amazonaws.networkmanager#DeleteResourcePolicyRequest``."""

from typing import TYPE_CHECKING, TypedDict

if TYPE_CHECKING:
    import aws_sdk_networkmanager.types.resource_arn


class DeleteResourcePolicyRequest(TypedDict):
    resource_arn: "aws_sdk_networkmanager.types.resource_arn.ResourceArn"
    """<p>The ARN of the policy to delete.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: DeleteResourcePolicyRequest) -> dict:
    out: dict = {}
    return out


def deserialize_json(data: dict) -> DeleteResourcePolicyRequest:
    out: DeleteResourcePolicyRequest = {}  # type: ignore[typeddict-item]
    return out
