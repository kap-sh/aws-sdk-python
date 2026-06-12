"""Generated from Smithy shape ``com.amazonaws.sagemakera2iruntime#DeleteHumanLoopRequest``."""

from typing import TYPE_CHECKING, TypedDict

if TYPE_CHECKING:
    import aws_sdk_sagemaker_a2i_runtime.types.human_loop_name


class DeleteHumanLoopRequest(TypedDict):
    human_loop_name: "aws_sdk_sagemaker_a2i_runtime.types.human_loop_name.HumanLoopName"
    """<p>The name of the human loop that you want to delete.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: DeleteHumanLoopRequest) -> dict:
    out: dict = {}
    return out


def deserialize_json(data: dict) -> DeleteHumanLoopRequest:
    out: DeleteHumanLoopRequest = {}  # type: ignore[typeddict-item]
    return out
