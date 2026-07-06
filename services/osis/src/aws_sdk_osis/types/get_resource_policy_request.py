"""Generated from Smithy shape ``com.amazonaws.osis#GetResourcePolicyRequest``."""

from typing import TYPE_CHECKING

from typing_extensions import TypedDict

if TYPE_CHECKING:
    import aws_sdk_osis.types.pipeline_arn


class GetResourcePolicyRequest(TypedDict, closed=True):
    resource_arn: "aws_sdk_osis.types.pipeline_arn.PipelineArn"
    """<p>The Amazon Resource Name (ARN) of the resource for which to retrieve the policy.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: GetResourcePolicyRequest) -> dict:
    out: dict = {}
    return out


def deserialize_json(data: dict) -> GetResourcePolicyRequest:
    out: GetResourcePolicyRequest = {}  # type: ignore[typeddict-item]
    return out
