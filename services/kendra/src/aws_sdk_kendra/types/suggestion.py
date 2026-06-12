"""Generated from Smithy shape ``com.amazonaws.kendra#Suggestion``."""

from typing import TYPE_CHECKING, TypedDict

from typing_extensions import NotRequired

if TYPE_CHECKING:
    import aws_sdk_kendra.types.result_id
    import aws_sdk_kendra.types.source_documents
    import aws_sdk_kendra.types.suggestion_value


class Suggestion(TypedDict):
    id: NotRequired["aws_sdk_kendra.types.result_id.ResultId"]
    """<p>The UUID (universally unique identifier) of a single query suggestion.</p>"""
    value: NotRequired["aws_sdk_kendra.types.suggestion_value.SuggestionValue"]
    """<p>The value for the UUID (universally unique identifier) of a single query suggestion.</p> <p>The value is the text string of a suggestion.</p>"""
    source_documents: NotRequired[
        "aws_sdk_kendra.types.source_documents.SourceDocuments"
    ]
    """<p>The list of document IDs and their fields/attributes that are used for a single query suggestion, if document fields set to use for query suggestions.</p>"""


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: Suggestion) -> dict:
    out: dict = {}
    if "id" in value:
        out["Id"] = value["id"]
    if "value" in value:
        import aws_sdk_kendra.types.suggestion_value

        out["Value"] = aws_sdk_kendra.types.suggestion_value.serialize_aws_json_1_1(
            value["value"]
        )
    if "source_documents" in value:
        import aws_sdk_kendra.types.source_documents

        out["SourceDocuments"] = (
            aws_sdk_kendra.types.source_documents.serialize_aws_json_1_1(
                value["source_documents"]
            )
        )
    return out


def deserialize_aws_json_1_1(data: dict) -> Suggestion:
    out: Suggestion = {}  # type: ignore[typeddict-item]
    if "Id" in data:
        out["id"] = data["Id"]
    if "Value" in data:
        import aws_sdk_kendra.types.suggestion_value

        out["value"] = aws_sdk_kendra.types.suggestion_value.deserialize_aws_json_1_1(
            data["Value"]
        )
    if "SourceDocuments" in data:
        import aws_sdk_kendra.types.source_documents

        out["source_documents"] = (
            aws_sdk_kendra.types.source_documents.deserialize_aws_json_1_1(
                data["SourceDocuments"]
            )
        )
    return out
