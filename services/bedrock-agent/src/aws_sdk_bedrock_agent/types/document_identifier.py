"""Generated from Smithy shape ``com.amazonaws.bedrockagent#DocumentIdentifier``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

from aws_sdk_bedrock_agent.errors import DeserializationError

if TYPE_CHECKING:
    import aws_sdk_bedrock_agent.types.content_data_source_type
    import aws_sdk_bedrock_agent.types.custom_document_identifier
    import aws_sdk_bedrock_agent.types.s3_location


class DocumentIdentifier(TypedDict, closed=True):
    data_source_type: (
        "aws_sdk_bedrock_agent.types.content_data_source_type.ContentDataSourceType"
    )
    """<p>The type of data source connected to the knowledge base that contains the document.</p>"""
    s3: NotRequired["aws_sdk_bedrock_agent.types.s3_location.S3Location"]
    """<p>Contains information that identifies the document in an S3 data source.</p>"""
    custom: NotRequired[
        "aws_sdk_bedrock_agent.types.custom_document_identifier.CustomDocumentIdentifier"
    ]
    """<p>Contains information that identifies the document in a custom data source.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: DocumentIdentifier) -> dict:
    out: dict = {}
    import aws_sdk_bedrock_agent.types.content_data_source_type

    out["dataSourceType"] = (
        aws_sdk_bedrock_agent.types.content_data_source_type.serialize_json(
            value["data_source_type"]
        )
    )
    if "s3" in value:
        import aws_sdk_bedrock_agent.types.s3_location

        out["s3"] = aws_sdk_bedrock_agent.types.s3_location.serialize_json(value["s3"])
    if "custom" in value:
        import aws_sdk_bedrock_agent.types.custom_document_identifier

        out["custom"] = (
            aws_sdk_bedrock_agent.types.custom_document_identifier.serialize_json(
                value["custom"]
            )
        )
    return out


def deserialize_json(data: dict) -> DocumentIdentifier:
    out: DocumentIdentifier = {}  # type: ignore[typeddict-item]
    if "dataSourceType" in data:
        import aws_sdk_bedrock_agent.types.content_data_source_type

        out["data_source_type"] = (
            aws_sdk_bedrock_agent.types.content_data_source_type.deserialize_json(
                data["dataSourceType"]
            )
        )
    else:
        raise DeserializationError("DocumentIdentifier.data_source_type required")
    if "s3" in data:
        import aws_sdk_bedrock_agent.types.s3_location

        out["s3"] = aws_sdk_bedrock_agent.types.s3_location.deserialize_json(data["s3"])
    if "custom" in data:
        import aws_sdk_bedrock_agent.types.custom_document_identifier

        out["custom"] = (
            aws_sdk_bedrock_agent.types.custom_document_identifier.deserialize_json(
                data["custom"]
            )
        )
    return out
