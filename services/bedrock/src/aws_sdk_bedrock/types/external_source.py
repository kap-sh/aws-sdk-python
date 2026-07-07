"""Generated from Smithy shape ``com.amazonaws.bedrock#ExternalSource``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

from aws_sdk_bedrock.errors import DeserializationError

if TYPE_CHECKING:
    import aws_sdk_bedrock.types.byte_content_doc
    import aws_sdk_bedrock.types.external_source_type
    import aws_sdk_bedrock.types.s3_object_doc


class ExternalSource(TypedDict, closed=True):
    source_type: "aws_sdk_bedrock.types.external_source_type.ExternalSourceType"
    """<p>The source type of the external source wrapper object.</p>"""
    s3_location: NotRequired["aws_sdk_bedrock.types.s3_object_doc.S3ObjectDoc"]
    """<p>The S3 location of the external source wrapper object.</p>"""
    byte_content: NotRequired["aws_sdk_bedrock.types.byte_content_doc.ByteContentDoc"]
    """<p>The identifier, content type, and data of the external source wrapper object.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: ExternalSource) -> dict:
    out: dict = {}
    import aws_sdk_bedrock.types.external_source_type

    out["sourceType"] = aws_sdk_bedrock.types.external_source_type.serialize_json(
        value["source_type"]
    )
    if "s3_location" in value:
        import aws_sdk_bedrock.types.s3_object_doc

        out["s3Location"] = aws_sdk_bedrock.types.s3_object_doc.serialize_json(
            value["s3_location"]
        )
    if "byte_content" in value:
        import aws_sdk_bedrock.types.byte_content_doc

        out["byteContent"] = aws_sdk_bedrock.types.byte_content_doc.serialize_json(
            value["byte_content"]
        )
    return out


def deserialize_json(data: dict) -> ExternalSource:
    out: ExternalSource = {}  # type: ignore[typeddict-item]
    if "sourceType" in data:
        import aws_sdk_bedrock.types.external_source_type

        out["source_type"] = (
            aws_sdk_bedrock.types.external_source_type.deserialize_json(
                data["sourceType"]
            )
        )
    else:
        raise DeserializationError("ExternalSource.source_type required")
    if "s3Location" in data:
        import aws_sdk_bedrock.types.s3_object_doc

        out["s3_location"] = aws_sdk_bedrock.types.s3_object_doc.deserialize_json(
            data["s3Location"]
        )
    if "byteContent" in data:
        import aws_sdk_bedrock.types.byte_content_doc

        out["byte_content"] = aws_sdk_bedrock.types.byte_content_doc.deserialize_json(
            data["byteContent"]
        )
    return out
