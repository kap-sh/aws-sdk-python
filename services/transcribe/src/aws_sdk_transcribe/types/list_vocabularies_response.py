"""Generated from Smithy shape ``com.amazonaws.transcribe#ListVocabulariesResponse``."""

from typing import TYPE_CHECKING, TypedDict

from typing_extensions import NotRequired

if TYPE_CHECKING:
    import aws_sdk_transcribe.types.next_token
    import aws_sdk_transcribe.types.vocabularies
    import aws_sdk_transcribe.types.vocabulary_state


class ListVocabulariesResponse(TypedDict):
    status: NotRequired["aws_sdk_transcribe.types.vocabulary_state.VocabularyState"]
    """<p>Lists all custom vocabularies that have the status specified in your request. Vocabularies are ordered by creation date, with the newest vocabulary first.</p>"""
    next_token: NotRequired["aws_sdk_transcribe.types.next_token.NextToken"]
    """<p>If <code>NextToken</code> is present in your response, it indicates that not all results are displayed. To view the next set of results, copy the string associated with the <code>NextToken</code> parameter in your results output, then run your request again including <code>NextToken</code> with the value of the copied string. Repeat as needed to view all your results.</p>"""
    vocabularies: NotRequired["aws_sdk_transcribe.types.vocabularies.Vocabularies"]
    """<p>Provides information about the custom vocabularies that match the criteria specified in your request.</p>"""


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: ListVocabulariesResponse) -> dict:
    out: dict = {}
    if "status" in value:
        import aws_sdk_transcribe.types.vocabulary_state

        out["Status"] = (
            aws_sdk_transcribe.types.vocabulary_state.serialize_aws_json_1_1(
                value["status"]
            )
        )
    if "next_token" in value:
        out["NextToken"] = value["next_token"]
    if "vocabularies" in value:
        import aws_sdk_transcribe.types.vocabularies

        out["Vocabularies"] = (
            aws_sdk_transcribe.types.vocabularies.serialize_aws_json_1_1(
                value["vocabularies"]
            )
        )
    return out


def deserialize_aws_json_1_1(data: dict) -> ListVocabulariesResponse:
    out: ListVocabulariesResponse = {}  # type: ignore[typeddict-item]
    if "Status" in data:
        import aws_sdk_transcribe.types.vocabulary_state

        out["status"] = (
            aws_sdk_transcribe.types.vocabulary_state.deserialize_aws_json_1_1(
                data["Status"]
            )
        )
    if "NextToken" in data:
        out["next_token"] = data["NextToken"]
    if "Vocabularies" in data:
        import aws_sdk_transcribe.types.vocabularies

        out["vocabularies"] = (
            aws_sdk_transcribe.types.vocabularies.deserialize_aws_json_1_1(
                data["Vocabularies"]
            )
        )
    return out
