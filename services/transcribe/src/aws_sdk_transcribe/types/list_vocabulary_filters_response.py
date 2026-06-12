"""Generated from Smithy shape ``com.amazonaws.transcribe#ListVocabularyFiltersResponse``."""

from typing import TYPE_CHECKING, TypedDict

from typing_extensions import NotRequired

if TYPE_CHECKING:
    import aws_sdk_transcribe.types.next_token
    import aws_sdk_transcribe.types.vocabulary_filters


class ListVocabularyFiltersResponse(TypedDict):
    next_token: NotRequired["aws_sdk_transcribe.types.next_token.NextToken"]
    """<p>If <code>NextToken</code> is present in your response, it indicates that not all results are displayed. To view the next set of results, copy the string associated with the <code>NextToken</code> parameter in your results output, then run your request again including <code>NextToken</code> with the value of the copied string. Repeat as needed to view all your results.</p>"""
    vocabulary_filters: NotRequired[
        "aws_sdk_transcribe.types.vocabulary_filters.VocabularyFilters"
    ]
    """<p>Provides information about the custom vocabulary filters that match the criteria specified in your request.</p>"""


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: ListVocabularyFiltersResponse) -> dict:
    out: dict = {}
    if "next_token" in value:
        out["NextToken"] = value["next_token"]
    if "vocabulary_filters" in value:
        import aws_sdk_transcribe.types.vocabulary_filters

        out["VocabularyFilters"] = (
            aws_sdk_transcribe.types.vocabulary_filters.serialize_aws_json_1_1(
                value["vocabulary_filters"]
            )
        )
    return out


def deserialize_aws_json_1_1(data: dict) -> ListVocabularyFiltersResponse:
    out: ListVocabularyFiltersResponse = {}  # type: ignore[typeddict-item]
    if "NextToken" in data:
        out["next_token"] = data["NextToken"]
    if "VocabularyFilters" in data:
        import aws_sdk_transcribe.types.vocabulary_filters

        out["vocabulary_filters"] = (
            aws_sdk_transcribe.types.vocabulary_filters.deserialize_aws_json_1_1(
                data["VocabularyFilters"]
            )
        )
    return out
