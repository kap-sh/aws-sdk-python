"""Generated from Smithy shape ``com.amazonaws.sagemakera2iruntime#StopHumanLoopRequest``."""

from typing import TYPE_CHECKING, TypedDict

from typing_extensions import NotRequired

if TYPE_CHECKING:
    import aws_sdk_sagemaker_a2i_runtime.types.human_loop_name


class StopHumanLoopRequest(TypedDict):
    human_loop_name: NotRequired[
        "aws_sdk_sagemaker_a2i_runtime.types.human_loop_name.HumanLoopName"
    ]
    """<p>The name of the human loop that you want to stop.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: StopHumanLoopRequest) -> dict:
    out: dict = {}
    if "human_loop_name" in value:
        out["HumanLoopName"] = value["human_loop_name"]
    return out


def deserialize_json(data: dict) -> StopHumanLoopRequest:
    out: StopHumanLoopRequest = {}  # type: ignore[typeddict-item]
    if "HumanLoopName" in data:
        out["human_loop_name"] = data["HumanLoopName"]
    return out
