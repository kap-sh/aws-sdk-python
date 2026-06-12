"""Generated from Smithy shape ``com.amazonaws.polly#StartSpeechSynthesisTaskOutput``."""

from typing import TYPE_CHECKING, TypedDict

from typing_extensions import NotRequired

if TYPE_CHECKING:
    import aws_sdk_polly.types.synthesis_task


class StartSpeechSynthesisTaskOutput(TypedDict):
    synthesis_task: NotRequired["aws_sdk_polly.types.synthesis_task.SynthesisTask"]
    """<p>SynthesisTask object that provides information and attributes about a newly submitted speech synthesis task.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: StartSpeechSynthesisTaskOutput) -> dict:
    out: dict = {}
    if "synthesis_task" in value:
        import aws_sdk_polly.types.synthesis_task

        out["SynthesisTask"] = aws_sdk_polly.types.synthesis_task.serialize_json(
            value["synthesis_task"]
        )
    return out


def deserialize_json(data: dict) -> StartSpeechSynthesisTaskOutput:
    out: StartSpeechSynthesisTaskOutput = {}  # type: ignore[typeddict-item]
    if "SynthesisTask" in data:
        import aws_sdk_polly.types.synthesis_task

        out["synthesis_task"] = aws_sdk_polly.types.synthesis_task.deserialize_json(
            data["SynthesisTask"]
        )
    return out
