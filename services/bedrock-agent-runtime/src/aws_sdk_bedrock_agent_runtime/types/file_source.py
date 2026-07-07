"""Generated from Smithy shape ``com.amazonaws.bedrockagentruntime#FileSource``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

from aws_sdk_bedrock_agent_runtime.errors import DeserializationError

if TYPE_CHECKING:
    import aws_sdk_bedrock_agent_runtime.types.byte_content_file
    import aws_sdk_bedrock_agent_runtime.types.file_source_type
    import aws_sdk_bedrock_agent_runtime.types.s3_object_file


class FileSource(TypedDict, closed=True):
    source_type: "aws_sdk_bedrock_agent_runtime.types.file_source_type.FileSourceType"
    """<p>The source type of the files to attach.</p>"""
    s3_location: NotRequired[
        "aws_sdk_bedrock_agent_runtime.types.s3_object_file.S3ObjectFile"
    ]
    """<p>The s3 location of the files to attach.</p>"""
    byte_content: NotRequired[
        "aws_sdk_bedrock_agent_runtime.types.byte_content_file.ByteContentFile"
    ]
    """<p>The data and the text of the attached files.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: FileSource) -> dict:
    out: dict = {}
    import aws_sdk_bedrock_agent_runtime.types.file_source_type

    out["sourceType"] = (
        aws_sdk_bedrock_agent_runtime.types.file_source_type.serialize_json(
            value["source_type"]
        )
    )
    if "s3_location" in value:
        import aws_sdk_bedrock_agent_runtime.types.s3_object_file

        out["s3Location"] = (
            aws_sdk_bedrock_agent_runtime.types.s3_object_file.serialize_json(
                value["s3_location"]
            )
        )
    if "byte_content" in value:
        import aws_sdk_bedrock_agent_runtime.types.byte_content_file

        out["byteContent"] = (
            aws_sdk_bedrock_agent_runtime.types.byte_content_file.serialize_json(
                value["byte_content"]
            )
        )
    return out


def deserialize_json(data: dict) -> FileSource:
    out: FileSource = {}  # type: ignore[typeddict-item]
    if "sourceType" in data:
        import aws_sdk_bedrock_agent_runtime.types.file_source_type

        out["source_type"] = (
            aws_sdk_bedrock_agent_runtime.types.file_source_type.deserialize_json(
                data["sourceType"]
            )
        )
    else:
        raise DeserializationError("FileSource.source_type required")
    if "s3Location" in data:
        import aws_sdk_bedrock_agent_runtime.types.s3_object_file

        out["s3_location"] = (
            aws_sdk_bedrock_agent_runtime.types.s3_object_file.deserialize_json(
                data["s3Location"]
            )
        )
    if "byteContent" in data:
        import aws_sdk_bedrock_agent_runtime.types.byte_content_file

        out["byte_content"] = (
            aws_sdk_bedrock_agent_runtime.types.byte_content_file.deserialize_json(
                data["byteContent"]
            )
        )
    return out
