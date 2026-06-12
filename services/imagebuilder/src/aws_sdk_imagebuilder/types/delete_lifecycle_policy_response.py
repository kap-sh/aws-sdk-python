"""Generated from Smithy shape ``com.amazonaws.imagebuilder#DeleteLifecyclePolicyResponse``."""

from typing import TYPE_CHECKING, TypedDict

from typing_extensions import NotRequired

if TYPE_CHECKING:
    import aws_sdk_imagebuilder.types.lifecycle_policy_arn


class DeleteLifecyclePolicyResponse(TypedDict):
    lifecycle_policy_arn: NotRequired[
        "aws_sdk_imagebuilder.types.lifecycle_policy_arn.LifecyclePolicyArn"
    ]
    """<p>The Amazon Resource Name (ARN) of the lifecycle policy that was deleted.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: DeleteLifecyclePolicyResponse) -> dict:
    out: dict = {}
    if "lifecycle_policy_arn" in value:
        out["lifecyclePolicyArn"] = value["lifecycle_policy_arn"]
    return out


def deserialize_json(data: dict) -> DeleteLifecyclePolicyResponse:
    out: DeleteLifecyclePolicyResponse = {}  # type: ignore[typeddict-item]
    if "lifecyclePolicyArn" in data:
        out["lifecycle_policy_arn"] = data["lifecyclePolicyArn"]
    return out
