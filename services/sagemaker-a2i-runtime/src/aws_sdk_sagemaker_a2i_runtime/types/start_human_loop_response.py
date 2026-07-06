"""Generated from Smithy shape ``com.amazonaws.sagemakera2iruntime#StartHumanLoopResponse``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import aws_sdk_sagemaker_a2i_runtime.types.human_loop_arn


class StartHumanLoopResponse(TypedDict, closed=True):
    human_loop_arn: NotRequired[
        "aws_sdk_sagemaker_a2i_runtime.types.human_loop_arn.HumanLoopArn"
    ]
    """<p>The Amazon Resource Name (ARN) of the human loop.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: StartHumanLoopResponse) -> dict:
    out: dict = {}
    if "human_loop_arn" in value:
        out["HumanLoopArn"] = value["human_loop_arn"]
    return out


def deserialize_json(data: dict) -> StartHumanLoopResponse:
    out: StartHumanLoopResponse = {}  # type: ignore[typeddict-item]
    if "HumanLoopArn" in data:
        out["human_loop_arn"] = data["HumanLoopArn"]
    return out
