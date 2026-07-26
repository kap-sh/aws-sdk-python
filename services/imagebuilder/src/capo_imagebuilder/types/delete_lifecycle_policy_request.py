"""Generated from Smithy shape ``com.amazonaws.imagebuilder#DeleteLifecyclePolicyRequest``."""

from typing import TYPE_CHECKING

from typing_extensions import TypedDict

if TYPE_CHECKING:
    import capo_imagebuilder.types.lifecycle_policy_arn


class DeleteLifecyclePolicyRequest(TypedDict, closed=True):
    lifecycle_policy_arn: (
        "capo_imagebuilder.types.lifecycle_policy_arn.LifecyclePolicyArn"
    )
    """<p>The Amazon Resource Name (ARN) of the lifecycle policy resource to delete.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: DeleteLifecyclePolicyRequest) -> dict:
    out: dict = {}
    return out


def deserialize_json(data: dict) -> DeleteLifecyclePolicyRequest:
    out: DeleteLifecyclePolicyRequest = {}  # type: ignore[typeddict-item]
    return out
