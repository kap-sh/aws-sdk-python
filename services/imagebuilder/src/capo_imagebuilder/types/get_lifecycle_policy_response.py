"""Generated from Smithy shape ``com.amazonaws.imagebuilder#GetLifecyclePolicyResponse``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import capo_imagebuilder.types.lifecycle_policy


class GetLifecyclePolicyResponse(TypedDict, closed=True):
    lifecycle_policy: NotRequired[
        "capo_imagebuilder.types.lifecycle_policy.LifecyclePolicy"
    ]
    """<p>The Amazon Resource Name (ARN) of the image lifecycle policy resource that was returned.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: GetLifecyclePolicyResponse) -> dict:
    out: dict = {}
    if "lifecycle_policy" in value:
        import capo_imagebuilder.types.lifecycle_policy

        out["lifecyclePolicy"] = (
            capo_imagebuilder.types.lifecycle_policy.serialize_json(
                value["lifecycle_policy"]
            )
        )
    return out


def deserialize_json(data: dict) -> GetLifecyclePolicyResponse:
    out: GetLifecyclePolicyResponse = {}  # type: ignore[typeddict-item]
    if "lifecyclePolicy" in data:
        import capo_imagebuilder.types.lifecycle_policy

        out["lifecycle_policy"] = (
            capo_imagebuilder.types.lifecycle_policy.deserialize_json(
                data["lifecyclePolicy"]
            )
        )
    return out
