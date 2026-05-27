"""Generated from Smithy shape ``com.amazonaws.lambda#DocumentDBEventSourceConfig``."""

from typing import TYPE_CHECKING, TypedDict
from typing_extensions import NotRequired

if TYPE_CHECKING:
    import aws_sdk_lambda.types.collection_name
    import aws_sdk_lambda.types.database_name
    import aws_sdk_lambda.types.full_document


class DocumentDBEventSourceConfig(TypedDict):
    database_name: NotRequired["aws_sdk_lambda.types.database_name.DatabaseName"]
    """<p> The name of the database to consume within the DocumentDB cluster. </p>"""
    collection_name: NotRequired["aws_sdk_lambda.types.collection_name.CollectionName"]
    """<p> The name of the collection to consume within the database. If you do not specify a collection, Lambda consumes all collections. </p>"""
    full_document: NotRequired["aws_sdk_lambda.types.full_document.FullDocument"]
    """<p> Determines what DocumentDB sends to your event stream during document update operations. If set to UpdateLookup, DocumentDB sends a delta describing the changes, along with a copy of the entire document. Otherwise, DocumentDB sends only a partial document that contains the changes. </p>"""


# --- restJson1 ser/de ---
def serialize_json(value: DocumentDBEventSourceConfig) -> dict:
    out: dict = {}
    if "database_name" in value:
        out["DatabaseName"] = value["database_name"]
    if "collection_name" in value:
        out["CollectionName"] = value["collection_name"]
    if "full_document" in value:
        import aws_sdk_lambda.types.full_document

        out["FullDocument"] = aws_sdk_lambda.types.full_document.serialize_json(
            value["full_document"]
        )
    return out


def deserialize_json(data: dict) -> DocumentDBEventSourceConfig:
    out: DocumentDBEventSourceConfig = {}  # type: ignore[typeddict-item]
    if "DatabaseName" in data:
        out["database_name"] = data["DatabaseName"]
    if "CollectionName" in data:
        out["collection_name"] = data["CollectionName"]
    if "FullDocument" in data:
        import aws_sdk_lambda.types.full_document

        out["full_document"] = aws_sdk_lambda.types.full_document.deserialize_json(
            data["FullDocument"]
        )
    return out
