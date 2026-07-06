"""Generated from Smithy shape ``com.amazonaws.polly#GetSpeechSynthesisTaskInput``."""

from typing import TYPE_CHECKING

from typing_extensions import TypedDict

if TYPE_CHECKING:
    import aws_sdk_polly.types.task_id


class GetSpeechSynthesisTaskInput(TypedDict, closed=True):
    task_id: "aws_sdk_polly.types.task_id.TaskId"
    """<p>The Amazon Polly generated identifier for a speech synthesis task.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: GetSpeechSynthesisTaskInput) -> dict:
    out: dict = {}
    return out


def deserialize_json(data: dict) -> GetSpeechSynthesisTaskInput:
    out: GetSpeechSynthesisTaskInput = {}  # type: ignore[typeddict-item]
    return out
