"""Generated from Smithy shape ``com.amazonaws.bedrockagent#CustomContent``."""

from typing import TYPE_CHECKING, TypedDict

from typing_extensions import NotRequired

from aws_sdk_bedrock_agent.errors import DeserializationError

if TYPE_CHECKING:
    import aws_sdk_bedrock_agent.types.custom_document_identifier
    import aws_sdk_bedrock_agent.types.custom_s3_location
    import aws_sdk_bedrock_agent.types.custom_source_type
    import aws_sdk_bedrock_agent.types.inline_content


class CustomContent(TypedDict):
    custom_document_identifier: "aws_sdk_bedrock_agent.types.custom_document_identifier.CustomDocumentIdentifier"
    """<p>A unique identifier for the document.</p>"""
    source_type: "aws_sdk_bedrock_agent.types.custom_source_type.CustomSourceType"
    """<p>The source of the data to ingest.</p>"""
    s3_location: NotRequired[
        "aws_sdk_bedrock_agent.types.custom_s3_location.CustomS3Location"
    ]
    """<p>Contains information about the Amazon S3 location of the file from which to ingest data.</p>"""
    inline_content: NotRequired[
        "aws_sdk_bedrock_agent.types.inline_content.InlineContent"
    ]
    """<p>Contains information about content defined inline to ingest into a knowledge base.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: CustomContent) -> dict:
    out: dict = {}
    import aws_sdk_bedrock_agent.types.custom_document_identifier

    out["customDocumentIdentifier"] = (
        aws_sdk_bedrock_agent.types.custom_document_identifier.serialize_json(
            value["custom_document_identifier"]
        )
    )
    import aws_sdk_bedrock_agent.types.custom_source_type

    out["sourceType"] = aws_sdk_bedrock_agent.types.custom_source_type.serialize_json(
        value["source_type"]
    )
    if "s3_location" in value:
        import aws_sdk_bedrock_agent.types.custom_s3_location

        out["s3Location"] = (
            aws_sdk_bedrock_agent.types.custom_s3_location.serialize_json(
                value["s3_location"]
            )
        )
    if "inline_content" in value:
        import aws_sdk_bedrock_agent.types.inline_content

        out["inlineContent"] = (
            aws_sdk_bedrock_agent.types.inline_content.serialize_json(
                value["inline_content"]
            )
        )
    return out


def deserialize_json(data: dict) -> CustomContent:
    out: CustomContent = {}  # type: ignore[typeddict-item]
    if "customDocumentIdentifier" in data:
        import aws_sdk_bedrock_agent.types.custom_document_identifier

        out["custom_document_identifier"] = (
            aws_sdk_bedrock_agent.types.custom_document_identifier.deserialize_json(
                data["customDocumentIdentifier"]
            )
        )
    else:
        raise DeserializationError("CustomContent.custom_document_identifier required")
    if "sourceType" in data:
        import aws_sdk_bedrock_agent.types.custom_source_type

        out["source_type"] = (
            aws_sdk_bedrock_agent.types.custom_source_type.deserialize_json(
                data["sourceType"]
            )
        )
    else:
        raise DeserializationError("CustomContent.source_type required")
    if "s3Location" in data:
        import aws_sdk_bedrock_agent.types.custom_s3_location

        out["s3_location"] = (
            aws_sdk_bedrock_agent.types.custom_s3_location.deserialize_json(
                data["s3Location"]
            )
        )
    if "inlineContent" in data:
        import aws_sdk_bedrock_agent.types.inline_content

        out["inline_content"] = (
            aws_sdk_bedrock_agent.types.inline_content.deserialize_json(
                data["inlineContent"]
            )
        )
    return out
