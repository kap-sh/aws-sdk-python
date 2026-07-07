"""Generated from Smithy shape ``com.amazonaws.transcribe#ListMedicalVocabulariesRequest``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import aws_sdk_transcribe.types.max_results
    import aws_sdk_transcribe.types.next_token
    import aws_sdk_transcribe.types.vocabulary_name
    import aws_sdk_transcribe.types.vocabulary_state


class ListMedicalVocabulariesRequest(TypedDict, closed=True):
    next_token: NotRequired["aws_sdk_transcribe.types.next_token.NextToken"]
    """<p>If your <code>ListMedicalVocabularies</code> request returns more results than can be displayed, <code>NextToken</code> is displayed in the response with an associated string. To get the next page of results, copy this string and repeat your request, including <code>NextToken</code> with the value of the copied string. Repeat as needed to view all your results.</p>"""
    max_results: NotRequired["aws_sdk_transcribe.types.max_results.MaxResults"]
    """<p>The maximum number of custom medical vocabularies to return in each page of results. If there are fewer results than the value that you specify, only the actual results are returned. If you do not specify a value, a default of 5 is used.</p>"""
    state_equals: NotRequired[
        "aws_sdk_transcribe.types.vocabulary_state.VocabularyState"
    ]
    """<p>Returns only custom medical vocabularies with the specified state. Custom vocabularies are ordered by creation date, with the newest vocabulary first. If you do not include <code>StateEquals</code>, all custom medical vocabularies are returned.</p>"""
    name_contains: NotRequired[
        "aws_sdk_transcribe.types.vocabulary_name.VocabularyName"
    ]
    """<p>Returns only the custom medical vocabularies that contain the specified string. The search is not case sensitive.</p>"""


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: ListMedicalVocabulariesRequest) -> dict:
    out: dict = {}
    return out


def deserialize_aws_json_1_1(data: dict) -> ListMedicalVocabulariesRequest:
    out: ListMedicalVocabulariesRequest = {}  # type: ignore[typeddict-item]
    return out
