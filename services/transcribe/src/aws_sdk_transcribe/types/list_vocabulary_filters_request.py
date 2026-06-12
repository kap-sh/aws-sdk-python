"""Generated from Smithy shape ``com.amazonaws.transcribe#ListVocabularyFiltersRequest``."""

from typing import TYPE_CHECKING, TypedDict

from typing_extensions import NotRequired

if TYPE_CHECKING:
    import aws_sdk_transcribe.types.max_results
    import aws_sdk_transcribe.types.next_token
    import aws_sdk_transcribe.types.vocabulary_filter_name


class ListVocabularyFiltersRequest(TypedDict):
    next_token: NotRequired["aws_sdk_transcribe.types.next_token.NextToken"]
    """<p>If your <code>ListVocabularyFilters</code> request returns more results than can be displayed, <code>NextToken</code> is displayed in the response with an associated string. To get the next page of results, copy this string and repeat your request, including <code>NextToken</code> with the value of the copied string. Repeat as needed to view all your results.</p>"""
    max_results: NotRequired["aws_sdk_transcribe.types.max_results.MaxResults"]
    """<p>The maximum number of custom vocabulary filters to return in each page of results. If there are fewer results than the value that you specify, only the actual results are returned. If you do not specify a value, a default of 5 is used.</p>"""
    name_contains: NotRequired[
        "aws_sdk_transcribe.types.vocabulary_filter_name.VocabularyFilterName"
    ]
    """<p>Returns only the custom vocabulary filters that contain the specified string. The search is not case sensitive.</p>"""


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: ListVocabularyFiltersRequest) -> dict:
    out: dict = {}
    return out


def deserialize_aws_json_1_1(data: dict) -> ListVocabularyFiltersRequest:
    out: ListVocabularyFiltersRequest = {}  # type: ignore[typeddict-item]
    return out
