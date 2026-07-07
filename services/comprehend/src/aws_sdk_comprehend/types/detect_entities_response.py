"""Generated from Smithy shape ``com.amazonaws.comprehend#DetectEntitiesResponse``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import aws_sdk_comprehend.types.document_metadata
    import aws_sdk_comprehend.types.list_of_blocks
    import aws_sdk_comprehend.types.list_of_document_type
    import aws_sdk_comprehend.types.list_of_entities
    import aws_sdk_comprehend.types.list_of_errors


class DetectEntitiesResponse(TypedDict, closed=True):
    entities: NotRequired["aws_sdk_comprehend.types.list_of_entities.ListOfEntities"]
    r"""<p>A collection of entities identified in the input text. For each entity, the response provides the entity text, entity type, where the entity text begins and ends, and the level of confidence that Amazon Comprehend has in the detection. </p> <p>If your request uses a custom entity recognition model, Amazon Comprehend detects the entities that the model is trained to recognize. Otherwise, it detects the default entity types. For a list of default entity types, see <a href=\"https://docs.aws.amazon.com/comprehend/latest/dg/how-entities.html\">Entities</a> in the Comprehend Developer Guide. </p>"""
    document_metadata: NotRequired[
        "aws_sdk_comprehend.types.document_metadata.DocumentMetadata"
    ]
    """<p>Information about the document, discovered during text extraction. This field is present in the response only if your request used the <code>Byte</code> parameter. </p>"""
    document_type: NotRequired[
        "aws_sdk_comprehend.types.list_of_document_type.ListOfDocumentType"
    ]
    """<p>The document type for each page in the input document. This field is present in the response only if your request used the <code>Byte</code> parameter. </p>"""
    blocks: NotRequired["aws_sdk_comprehend.types.list_of_blocks.ListOfBlocks"]
    """<p>Information about each block of text in the input document. Blocks are nested. A page block contains a block for each line of text, which contains a block for each word. </p> <p>The <code>Block</code> content for a Word input document does not include a <code>Geometry</code> field.</p> <p>The <code>Block</code> field is not present in the response for plain-text inputs.</p>"""
    errors: NotRequired["aws_sdk_comprehend.types.list_of_errors.ListOfErrors"]
    """<p>Page-level errors that the system detected while processing the input document. The field is empty if the system encountered no errors.</p>"""


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: DetectEntitiesResponse) -> dict:
    out: dict = {}
    if "entities" in value:
        import aws_sdk_comprehend.types.list_of_entities

        out["Entities"] = (
            aws_sdk_comprehend.types.list_of_entities.serialize_aws_json_1_1(
                value["entities"]
            )
        )
    if "document_metadata" in value:
        import aws_sdk_comprehend.types.document_metadata

        out["DocumentMetadata"] = (
            aws_sdk_comprehend.types.document_metadata.serialize_aws_json_1_1(
                value["document_metadata"]
            )
        )
    if "document_type" in value:
        import aws_sdk_comprehend.types.list_of_document_type

        out["DocumentType"] = (
            aws_sdk_comprehend.types.list_of_document_type.serialize_aws_json_1_1(
                value["document_type"]
            )
        )
    if "blocks" in value:
        import aws_sdk_comprehend.types.list_of_blocks

        out["Blocks"] = aws_sdk_comprehend.types.list_of_blocks.serialize_aws_json_1_1(
            value["blocks"]
        )
    if "errors" in value:
        import aws_sdk_comprehend.types.list_of_errors

        out["Errors"] = aws_sdk_comprehend.types.list_of_errors.serialize_aws_json_1_1(
            value["errors"]
        )
    return out


def deserialize_aws_json_1_1(data: dict) -> DetectEntitiesResponse:
    out: DetectEntitiesResponse = {}  # type: ignore[typeddict-item]
    if "Entities" in data:
        import aws_sdk_comprehend.types.list_of_entities

        out["entities"] = (
            aws_sdk_comprehend.types.list_of_entities.deserialize_aws_json_1_1(
                data["Entities"]
            )
        )
    if "DocumentMetadata" in data:
        import aws_sdk_comprehend.types.document_metadata

        out["document_metadata"] = (
            aws_sdk_comprehend.types.document_metadata.deserialize_aws_json_1_1(
                data["DocumentMetadata"]
            )
        )
    if "DocumentType" in data:
        import aws_sdk_comprehend.types.list_of_document_type

        out["document_type"] = (
            aws_sdk_comprehend.types.list_of_document_type.deserialize_aws_json_1_1(
                data["DocumentType"]
            )
        )
    if "Blocks" in data:
        import aws_sdk_comprehend.types.list_of_blocks

        out["blocks"] = (
            aws_sdk_comprehend.types.list_of_blocks.deserialize_aws_json_1_1(
                data["Blocks"]
            )
        )
    if "Errors" in data:
        import aws_sdk_comprehend.types.list_of_errors

        out["errors"] = (
            aws_sdk_comprehend.types.list_of_errors.deserialize_aws_json_1_1(
                data["Errors"]
            )
        )
    return out
