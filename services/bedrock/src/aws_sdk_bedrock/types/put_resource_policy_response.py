"""Generated from Smithy shape ``com.amazonaws.bedrock#PutResourcePolicyResponse``."""

from typing import TYPE_CHECKING, TypedDict

from typing_extensions import NotRequired

if TYPE_CHECKING:
    import aws_sdk_bedrock.types.resource_policy_resource_arn


class PutResourcePolicyResponse(TypedDict):
    resource_arn: NotRequired[
        "aws_sdk_bedrock.types.resource_policy_resource_arn.ResourcePolicyResourceArn"
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
    if "resourceArn" in data:
        out["resource_arn"] = data["resourceArn"]
    return out
