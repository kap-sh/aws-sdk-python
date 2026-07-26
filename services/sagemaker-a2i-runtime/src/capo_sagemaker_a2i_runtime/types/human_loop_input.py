"""Generated from Smithy shape ``com.amazonaws.sagemakera2iruntime#HumanLoopInput``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import capo_sagemaker_a2i_runtime.types.input_content


class HumanLoopInput(TypedDict, closed=True):
    input_content: NotRequired[
        "capo_sagemaker_a2i_runtime.types.input_content.InputContent"
    ]
    """<p>Serialized input from the human loop. The input must be a string representation of a file in JSON format.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: HumanLoopInput) -> dict:
    out: dict = {}
    if "input_content" in value:
        out["InputContent"] = value["input_content"]
    return out


def deserialize_json(data: dict) -> HumanLoopInput:
    out: HumanLoopInput = {}  # type: ignore[typeddict-item]
    if "InputContent" in data:
        out["input_content"] = data["InputContent"]
    return out
