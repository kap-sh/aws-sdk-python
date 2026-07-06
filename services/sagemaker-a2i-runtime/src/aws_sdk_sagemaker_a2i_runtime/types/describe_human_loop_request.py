"""Generated from Smithy shape ``com.amazonaws.sagemakera2iruntime#DescribeHumanLoopRequest``."""

from typing import TYPE_CHECKING

from typing_extensions import TypedDict

if TYPE_CHECKING:
    import aws_sdk_sagemaker_a2i_runtime.types.human_loop_name


class DescribeHumanLoopRequest(TypedDict, closed=True):
    human_loop_name: "aws_sdk_sagemaker_a2i_runtime.types.human_loop_name.HumanLoopName"
    """<p>The name of the human loop that you want information about.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: DescribeHumanLoopRequest) -> dict:
    out: dict = {}
    return out


def deserialize_json(data: dict) -> DescribeHumanLoopRequest:
    out: DescribeHumanLoopRequest = {}  # type: ignore[typeddict-item]
    return out
