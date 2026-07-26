"""Generated from Smithy shape ``com.amazonaws.polly#ListSpeechSynthesisTasksInput``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import capo_polly.types.max_results
    import capo_polly.types.next_token
    import capo_polly.types.task_status


class ListSpeechSynthesisTasksInput(TypedDict, closed=True):
    max_results: NotRequired["capo_polly.types.max_results.MaxResults"]
    """<p>Maximum number of speech synthesis tasks returned in a List operation.</p>"""
    next_token: NotRequired["capo_polly.types.next_token.NextToken"]
    """<p>The pagination token to use in the next request to continue the listing of speech synthesis tasks. </p>"""
    status: NotRequired["capo_polly.types.task_status.TaskStatus"]
    """<p>Status of the speech synthesis tasks returned in a List operation</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: ListSpeechSynthesisTasksInput) -> dict:
    out: dict = {}
    return out


def deserialize_json(data: dict) -> ListSpeechSynthesisTasksInput:
    out: ListSpeechSynthesisTasksInput = {}  # type: ignore[typeddict-item]
    return out
