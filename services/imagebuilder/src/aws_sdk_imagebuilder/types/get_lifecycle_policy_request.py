"""Generated from Smithy shape ``com.amazonaws.imagebuilder#GetLifecyclePolicyRequest``."""

from typing import TYPE_CHECKING, TypedDict

if TYPE_CHECKING:
    import aws_sdk_imagebuilder.types.lifecycle_policy_arn


class GetLifecyclePolicyRequest(TypedDict):
    lifecycle_policy_arn: (
        "aws_sdk_imagebuilder.types.lifecycle_policy_arn.LifecyclePolicyArn"
    )
    """<p>Specifies the Amazon Resource Name (ARN) of the image lifecycle policy resource to get.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: GetLifecyclePolicyRequest) -> dict:
    out: dict = {}
    return out


def deserialize_json(data: dict) -> GetLifecyclePolicyRequest:
    out: GetLifecyclePolicyRequest = {}  # type: ignore[typeddict-item]
    return out
