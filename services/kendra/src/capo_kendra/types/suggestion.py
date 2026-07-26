"""Generated from Smithy shape ``com.amazonaws.kendra#Suggestion``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import capo_kendra.types.result_id
    import capo_kendra.types.source_documents
    import capo_kendra.types.suggestion_value


class Suggestion(TypedDict, closed=True):
    id: NotRequired["capo_kendra.types.result_id.ResultId"]
    """<p>The UUID (universally unique identifier) of a single query suggestion.</p>"""
    value: NotRequired["capo_kendra.types.suggestion_value.SuggestionValue"]
    """<p>The value for the UUID (universally unique identifier) of a single query suggestion.</p> <p>The value is the text string of a suggestion.</p>"""
    source_documents: NotRequired["capo_kendra.types.source_documents.SourceDocuments"]
    """<p>The list of document IDs and their fields/attributes that are used for a single query suggestion, if document fields set to use for query suggestions.</p>"""


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: Suggestion) -> dict:
    out: dict = {}
    if "id" in value:
        out["Id"] = value["id"]
    if "value" in value:
        import capo_kendra.types.suggestion_value

        out["Value"] = capo_kendra.types.suggestion_value.serialize_aws_json_1_1(
            value["value"]
        )
    if "source_documents" in value:
        import capo_kendra.types.source_documents

        out["SourceDocuments"] = (
            capo_kendra.types.source_documents.serialize_aws_json_1_1(
                value["source_documents"]
            )
        )
    return out


def deserialize_aws_json_1_1(data: dict) -> Suggestion:
    out: Suggestion = {}  # type: ignore[typeddict-item]
    if "Id" in data:
        out["id"] = data["Id"]
    if "Value" in data:
        import capo_kendra.types.suggestion_value

        out["value"] = capo_kendra.types.suggestion_value.deserialize_aws_json_1_1(
            data["Value"]
        )
    if "SourceDocuments" in data:
        import capo_kendra.types.source_documents

        out["source_documents"] = (
            capo_kendra.types.source_documents.deserialize_aws_json_1_1(
                data["SourceDocuments"]
            )
        )
    return out
