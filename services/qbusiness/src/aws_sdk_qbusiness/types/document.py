"""Generated from Smithy shape ``com.amazonaws.qbusiness#Document``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

from aws_sdk_qbusiness.errors import DeserializationError

if TYPE_CHECKING:
    import aws_sdk_qbusiness.types.access_configuration
    import aws_sdk_qbusiness.types.content_type
    import aws_sdk_qbusiness.types.document_attributes
    import aws_sdk_qbusiness.types.document_content
    import aws_sdk_qbusiness.types.document_enrichment_configuration
    import aws_sdk_qbusiness.types.document_id
    import aws_sdk_qbusiness.types.media_extraction_configuration
    import aws_sdk_qbusiness.types.title


class Document(TypedDict, closed=True):
    id: "aws_sdk_qbusiness.types.document_id.DocumentId"
    """<p>The identifier of the document.</p>"""
    attributes: NotRequired[
        "aws_sdk_qbusiness.types.document_attributes.DocumentAttributes"
    ]
    """<p>Custom attributes to apply to the document for refining Amazon Q Business web experience responses.</p>"""
    content: NotRequired["aws_sdk_qbusiness.types.document_content.DocumentContent"]
    """<p>The contents of the document.</p>"""
    content_type: NotRequired["aws_sdk_qbusiness.types.content_type.ContentType"]
    """<p>The file type of the document in the Blob field.</p> <p>If you want to index snippets or subsets of HTML documents instead of the entirety of the HTML documents, you add the <code>HTML</code> start and closing tags (<code>&lt;HTML&gt;content&lt;/HTML&gt;</code>) around the content.</p>"""
    title: NotRequired["aws_sdk_qbusiness.types.title.Title"]
    """<p>The title of the document.</p>"""
    access_configuration: NotRequired[
        "aws_sdk_qbusiness.types.access_configuration.AccessConfiguration"
    ]
    """<p>Configuration information for access permission to a document.</p>"""
    document_enrichment_configuration: NotRequired[
        "aws_sdk_qbusiness.types.document_enrichment_configuration.DocumentEnrichmentConfiguration"
    ]
    """<p>The configuration information for altering document metadata and content during the document ingestion process.</p>"""
    media_extraction_configuration: NotRequired[
        "aws_sdk_qbusiness.types.media_extraction_configuration.MediaExtractionConfiguration"
    ]
    """<p>The configuration for extracting information from media in the document.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: Document) -> dict:
    out: dict = {}
    out["id"] = value["id"]
    if "attributes" in value:
        import aws_sdk_qbusiness.types.document_attributes

        out["attributes"] = aws_sdk_qbusiness.types.document_attributes.serialize_json(
            value["attributes"]
        )
    if "content" in value:
        import aws_sdk_qbusiness.types.document_content

        out["content"] = aws_sdk_qbusiness.types.document_content.serialize_json(
            value["content"]
        )
    if "content_type" in value:
        import aws_sdk_qbusiness.types.content_type

        out["contentType"] = aws_sdk_qbusiness.types.content_type.serialize_json(
            value["content_type"]
        )
    if "title" in value:
        out["title"] = value["title"]
    if "access_configuration" in value:
        import aws_sdk_qbusiness.types.access_configuration

        out["accessConfiguration"] = (
            aws_sdk_qbusiness.types.access_configuration.serialize_json(
                value["access_configuration"]
            )
        )
    if "document_enrichment_configuration" in value:
        import aws_sdk_qbusiness.types.document_enrichment_configuration

        out["documentEnrichmentConfiguration"] = (
            aws_sdk_qbusiness.types.document_enrichment_configuration.serialize_json(
                value["document_enrichment_configuration"]
            )
        )
    if "media_extraction_configuration" in value:
        import aws_sdk_qbusiness.types.media_extraction_configuration

        out["mediaExtractionConfiguration"] = (
            aws_sdk_qbusiness.types.media_extraction_configuration.serialize_json(
                value["media_extraction_configuration"]
            )
        )
    return out


def deserialize_json(data: dict) -> Document:
    out: Document = {}  # type: ignore[typeddict-item]
    if "id" in data:
        out["id"] = data["id"]
    else:
        raise DeserializationError("Document.id required")
    if "attributes" in data:
        import aws_sdk_qbusiness.types.document_attributes

        out["attributes"] = (
            aws_sdk_qbusiness.types.document_attributes.deserialize_json(
                data["attributes"]
            )
        )
    if "content" in data:
        import aws_sdk_qbusiness.types.document_content

        out["content"] = aws_sdk_qbusiness.types.document_content.deserialize_json(
            data["content"]
        )
    if "contentType" in data:
        import aws_sdk_qbusiness.types.content_type

        out["content_type"] = aws_sdk_qbusiness.types.content_type.deserialize_json(
            data["contentType"]
        )
    if "title" in data:
        out["title"] = data["title"]
    if "accessConfiguration" in data:
        import aws_sdk_qbusiness.types.access_configuration

        out["access_configuration"] = (
            aws_sdk_qbusiness.types.access_configuration.deserialize_json(
                data["accessConfiguration"]
            )
        )
    if "documentEnrichmentConfiguration" in data:
        import aws_sdk_qbusiness.types.document_enrichment_configuration

        out["document_enrichment_configuration"] = (
            aws_sdk_qbusiness.types.document_enrichment_configuration.deserialize_json(
                data["documentEnrichmentConfiguration"]
            )
        )
    if "mediaExtractionConfiguration" in data:
        import aws_sdk_qbusiness.types.media_extraction_configuration

        out["media_extraction_configuration"] = (
            aws_sdk_qbusiness.types.media_extraction_configuration.deserialize_json(
                data["mediaExtractionConfiguration"]
            )
        )
    return out
