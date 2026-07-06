"""Generated from Smithy shape ``com.amazonaws.polly#GetSpeechSynthesisTaskOutput``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import aws_sdk_polly.types.synthesis_task


class GetSpeechSynthesisTaskOutput(TypedDict, closed=True):
    synthesis_task: NotRequired["aws_sdk_polly.types.synthesis_task.SynthesisTask"]
    """<p>SynthesisTask object that provides information from the requested task, including output format, creation time, task status, and so on.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: GetSpeechSynthesisTaskOutput) -> dict:
    out: dict = {}
    if "synthesis_task" in value:
        import aws_sdk_polly.types.synthesis_task

        out["SynthesisTask"] = aws_sdk_polly.types.synthesis_task.serialize_json(
            value["synthesis_task"]
        )
    return out


def deserialize_json(data: dict) -> GetSpeechSynthesisTaskOutput:
    out: GetSpeechSynthesisTaskOutput = {}  # type: ignore[typeddict-item]
    if "SynthesisTask" in data:
        import aws_sdk_polly.types.synthesis_task

        out["synthesis_task"] = aws_sdk_polly.types.synthesis_task.deserialize_json(
            data["SynthesisTask"]
        )
    return out
