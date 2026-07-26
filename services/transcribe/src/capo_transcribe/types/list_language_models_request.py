"""Generated from Smithy shape ``com.amazonaws.transcribe#ListLanguageModelsRequest``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import capo_transcribe.types.max_results
    import capo_transcribe.types.model_name
    import capo_transcribe.types.model_status
    import capo_transcribe.types.next_token


class ListLanguageModelsRequest(TypedDict, closed=True):
    status_equals: NotRequired["capo_transcribe.types.model_status.ModelStatus"]
    """<p>Returns only custom language models with the specified status. Language models are ordered by creation date, with the newest model first. If you do not include <code>StatusEquals</code>, all custom language models are returned.</p>"""
    name_contains: NotRequired["capo_transcribe.types.model_name.ModelName"]
    """<p>Returns only the custom language models that contain the specified string. The search is not case sensitive.</p>"""
    next_token: NotRequired["capo_transcribe.types.next_token.NextToken"]
    """<p>If your <code>ListLanguageModels</code> request returns more results than can be displayed, <code>NextToken</code> is displayed in the response with an associated string. To get the next page of results, copy this string and repeat your request, including <code>NextToken</code> with the value of the copied string. Repeat as needed to view all your results.</p>"""
    max_results: NotRequired["capo_transcribe.types.max_results.MaxResults"]
    """<p>The maximum number of custom language models to return in each page of results. If there are fewer results than the value that you specify, only the actual results are returned. If you do not specify a value, a default of 5 is used.</p>"""


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: ListLanguageModelsRequest) -> dict:
    out: dict = {}
    return out


def deserialize_aws_json_1_1(data: dict) -> ListLanguageModelsRequest:
    out: ListLanguageModelsRequest = {}  # type: ignore[typeddict-item]
    return out
