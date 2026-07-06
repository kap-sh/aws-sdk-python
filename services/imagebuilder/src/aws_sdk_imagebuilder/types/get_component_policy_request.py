"""Generated from Smithy shape ``com.amazonaws.imagebuilder#GetComponentPolicyRequest``."""

from typing import TYPE_CHECKING

from typing_extensions import TypedDict

if TYPE_CHECKING:
    import aws_sdk_imagebuilder.types.component_build_version_arn


class GetComponentPolicyRequest(TypedDict, closed=True):
    component_arn: "aws_sdk_imagebuilder.types.component_build_version_arn.ComponentBuildVersionArn"
    """<p>The Amazon Resource Name (ARN) of the component whose policy you want to retrieve.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: GetComponentPolicyRequest) -> dict:
    out: dict = {}
    return out


def deserialize_json(data: dict) -> GetComponentPolicyRequest:
    out: GetComponentPolicyRequest = {}  # type: ignore[typeddict-item]
    return out
