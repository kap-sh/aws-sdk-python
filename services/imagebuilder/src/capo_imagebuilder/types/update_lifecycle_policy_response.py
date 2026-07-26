"""Generated from Smithy shape ``com.amazonaws.imagebuilder#UpdateLifecyclePolicyResponse``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import capo_imagebuilder.types.lifecycle_policy_arn


class UpdateLifecyclePolicyResponse(TypedDict, closed=True):
    lifecycle_policy_arn: NotRequired[
        "capo_imagebuilder.types.lifecycle_policy_arn.LifecyclePolicyArn"
    ]
    """<p>The Amazon Resource Name (ARN) of the image lifecycle policy resource that was updated.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: UpdateLifecyclePolicyResponse) -> dict:
    out: dict = {}
    if "lifecycle_policy_arn" in value:
        out["lifecyclePolicyArn"] = value["lifecycle_policy_arn"]
    return out


def deserialize_json(data: dict) -> UpdateLifecyclePolicyResponse:
    out: UpdateLifecyclePolicyResponse = {}  # type: ignore[typeddict-item]
    if "lifecyclePolicyArn" in data:
        out["lifecycle_policy_arn"] = data["lifecyclePolicyArn"]
    return out
