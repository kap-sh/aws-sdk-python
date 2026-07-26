"""Generated from Smithy shape ``com.amazonaws.osis#DeleteResourcePolicyRequest``."""

from typing import TYPE_CHECKING

from typing_extensions import TypedDict

if TYPE_CHECKING:
    import capo_osis.types.pipeline_arn


class DeleteResourcePolicyRequest(TypedDict, closed=True):
    resource_arn: "capo_osis.types.pipeline_arn.PipelineArn"
    """<p>The Amazon Resource Name (ARN) of the resource from which to delete the policy.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: DeleteResourcePolicyRequest) -> dict:
    out: dict = {}
    return out


def deserialize_json(data: dict) -> DeleteResourcePolicyRequest:
    out: DeleteResourcePolicyRequest = {}  # type: ignore[typeddict-item]
    return out
