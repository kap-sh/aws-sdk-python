"""Generated from Smithy shape ``com.amazonaws.polly#ListSpeechSynthesisTasksOutput``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import aws_sdk_polly.types.next_token
    import aws_sdk_polly.types.synthesis_tasks


class ListSpeechSynthesisTasksOutput(TypedDict, closed=True):
    next_token: NotRequired["aws_sdk_polly.types.next_token.NextToken"]
    """<p>An opaque pagination token returned from the previous List operation in this request. If present, this indicates where to continue the listing.</p>"""
    synthesis_tasks: NotRequired["aws_sdk_polly.types.synthesis_tasks.SynthesisTasks"]
    """<p>List of SynthesisTask objects that provides information from the specified task in the list request, including output format, creation time, task status, and so on.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: ListSpeechSynthesisTasksOutput) -> dict:
    out: dict = {}
    if "next_token" in value:
        out["NextToken"] = value["next_token"]
    if "synthesis_tasks" in value:
        import aws_sdk_polly.types.synthesis_tasks

        out["SynthesisTasks"] = aws_sdk_polly.types.synthesis_tasks.serialize_json(
            value["synthesis_tasks"]
        )
    return out


def deserialize_json(data: dict) -> ListSpeechSynthesisTasksOutput:
    out: ListSpeechSynthesisTasksOutput = {}  # type: ignore[typeddict-item]
    if "NextToken" in data:
        out["next_token"] = data["NextToken"]
    if "SynthesisTasks" in data:
        import aws_sdk_polly.types.synthesis_tasks

        out["synthesis_tasks"] = aws_sdk_polly.types.synthesis_tasks.deserialize_json(
            data["SynthesisTasks"]
        )
    return out
