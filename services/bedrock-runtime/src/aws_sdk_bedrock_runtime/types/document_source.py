"""Generated from Smithy shape ``com.amazonaws.bedrockruntime#DocumentSource``."""

from typing import TYPE_CHECKING, TypeAlias

from typing_extensions import TypedDict

from aws_sdk_bedrock_runtime.errors import DeserializationError, SerializationError

if TYPE_CHECKING:
    import aws_sdk_bedrock_runtime.types.document_content_blocks
    import aws_sdk_bedrock_runtime.types.s3_location


class _DocumentSource_bytes(TypedDict, closed=True):
    bytes: "bytes"


class _DocumentSource_s3Location(TypedDict, closed=True):
    s3Location: "aws_sdk_bedrock_runtime.types.s3_location.S3Location"


class _DocumentSource_text(TypedDict, closed=True):
    text: "str"


class _DocumentSource_content(TypedDict, closed=True):
    content: (
        "aws_sdk_bedrock_runtime.types.document_content_blocks.DocumentContentBlocks"
    )


DocumentSource: TypeAlias = (
    _DocumentSource_bytes
    | _DocumentSource_s3Location
    | _DocumentSource_text
    | _DocumentSource_content
)


# --- restJson1 ser/de ---
def serialize_json(value: DocumentSource) -> dict:
    if "bytes" in value:
        import aws_sdk_bedrock_runtime.types._prelude.blob

        return {
            "bytes": aws_sdk_bedrock_runtime.types._prelude.blob.serialize_json(
                value["bytes"]
            )
        }
    elif "s3Location" in value:
        import aws_sdk_bedrock_runtime.types.s3_location

        return {
            "s3Location": aws_sdk_bedrock_runtime.types.s3_location.serialize_json(
                value["s3Location"]
            )
        }
    elif "text" in value:
        return {"text": value["text"]}
    elif "content" in value:
        import aws_sdk_bedrock_runtime.types.document_content_blocks

        return {
            "content": aws_sdk_bedrock_runtime.types.document_content_blocks.serialize_json(
                value["content"]
            )
        }
    else:
        raise SerializationError("DocumentSource: no variant present")


def deserialize_json(data: dict) -> DocumentSource:
    if "bytes" in data:
        import aws_sdk_bedrock_runtime.types._prelude.blob

        return {
            "bytes": aws_sdk_bedrock_runtime.types._prelude.blob.deserialize_json(
                data["bytes"]
            )
        }
    elif "s3Location" in data:
        import aws_sdk_bedrock_runtime.types.s3_location

        return {
            "s3Location": aws_sdk_bedrock_runtime.types.s3_location.deserialize_json(
                data["s3Location"]
            )
        }
    elif "text" in data:
        return {"text": data["text"]}
    elif "content" in data:
        import aws_sdk_bedrock_runtime.types.document_content_blocks

        return {
            "content": aws_sdk_bedrock_runtime.types.document_content_blocks.deserialize_json(
                data["content"]
            )
        }
    else:
        raise DeserializationError("DocumentSource: no recognized variant key")
