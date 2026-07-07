"""Generated from Smithy shape ``com.amazonaws.connect#SearchVocabulariesResponse``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import aws_sdk_connect.types.vocabulary_next_token
    import aws_sdk_connect.types.vocabulary_summary_list


class SearchVocabulariesResponse(TypedDict, closed=True):
    vocabulary_summary_list: NotRequired[
        "aws_sdk_connect.types.vocabulary_summary_list.VocabularySummaryList"
    ]
    """<p>The list of the available custom vocabularies.</p>"""
    next_token: NotRequired[
        "aws_sdk_connect.types.vocabulary_next_token.VocabularyNextToken"
    ]
    """<p>If there are additional results, this is the token for the next set of results.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: SearchVocabulariesResponse) -> dict:
    out: dict = {}
    if "vocabulary_summary_list" in value:
        import aws_sdk_connect.types.vocabulary_summary_list

        out["VocabularySummaryList"] = (
            aws_sdk_connect.types.vocabulary_summary_list.serialize_json(
                value["vocabulary_summary_list"]
            )
        )
    if "next_token" in value:
        out["NextToken"] = value["next_token"]
    return out


def deserialize_json(data: dict) -> SearchVocabulariesResponse:
    out: SearchVocabulariesResponse = {}  # type: ignore[typeddict-item]
    if "VocabularySummaryList" in data:
        import aws_sdk_connect.types.vocabulary_summary_list

        out["vocabulary_summary_list"] = (
            aws_sdk_connect.types.vocabulary_summary_list.deserialize_json(
                data["VocabularySummaryList"]
            )
        )
    if "NextToken" in data:
        out["next_token"] = data["NextToken"]
    return out
