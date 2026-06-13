"""Generated from Smithy shape ``com.amazonaws.bedrockruntime#DocumentBlock``."""

from typing import TYPE_CHECKING, TypedDict

from typing_extensions import NotRequired

from aws_sdk_bedrock_runtime.errors import DeserializationError

if TYPE_CHECKING:
    import aws_sdk_bedrock_runtime.types.citations_config
    import aws_sdk_bedrock_runtime.types.document_format
    import aws_sdk_bedrock_runtime.types.document_source


class DocumentBlock(TypedDict):
    format: "aws_sdk_bedrock_runtime.types.document_format.DocumentFormat"
    """<p>The format of a document, or its extension.</p>"""
    name: "str"
    """<p>A name for the document. The name can only contain the following characters:</p> <ul> <li> <p>Alphanumeric characters</p> </li> <li> <p>Whitespace characters (no more than one in a row)</p> </li> <li> <p>Hyphens</p> </li> <li> <p>Parentheses</p> </li> <li> <p>Square brackets</p> </li> </ul> <note> <p>This field is vulnerable to prompt injections, because the model might inadvertently interpret it as instructions. Therefore, we recommend that you specify a neutral name.</p> </note>"""
    source: "aws_sdk_bedrock_runtime.types.document_source.DocumentSource"
    """<p>Contains the content of the document.</p>"""
    context: NotRequired["str"]
    """<p>Contextual information about how the document should be processed or interpreted by the model when generating citations.</p>"""
    citations: NotRequired[
        "aws_sdk_bedrock_runtime.types.citations_config.CitationsConfig"
    ]
    """<p>Configuration settings that control how citations should be generated for this specific document.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: DocumentBlock) -> dict:
    out: dict = {}
    import aws_sdk_bedrock_runtime.types.document_format

    out["format"] = aws_sdk_bedrock_runtime.types.document_format.serialize_json(
        value.get("format", "txt")
    )
    out["name"] = value["name"]
    import aws_sdk_bedrock_runtime.types.document_source

    out["source"] = aws_sdk_bedrock_runtime.types.document_source.serialize_json(
        value["source"]
    )
    if "context" in value:
        out["context"] = value["context"]
    if "citations" in value:
        import aws_sdk_bedrock_runtime.types.citations_config

        out["citations"] = (
            aws_sdk_bedrock_runtime.types.citations_config.serialize_json(
                value["citations"]
            )
        )
    return out


def deserialize_json(data: dict) -> DocumentBlock:
    out: DocumentBlock = {}  # type: ignore[typeddict-item]
    if "format" in data:
        import aws_sdk_bedrock_runtime.types.document_format

        out["format"] = aws_sdk_bedrock_runtime.types.document_format.deserialize_json(
            data["format"]
        )
    else:
        out["format"] = "txt"
    if "name" in data:
        out["name"] = data["name"]
    else:
        raise DeserializationError("DocumentBlock.name required")
    if "source" in data:
        import aws_sdk_bedrock_runtime.types.document_source

        out["source"] = aws_sdk_bedrock_runtime.types.document_source.deserialize_json(
            data["source"]
        )
    else:
        raise DeserializationError("DocumentBlock.source required")
    if "context" in data:
        out["context"] = data["context"]
    if "citations" in data:
        import aws_sdk_bedrock_runtime.types.citations_config

        out["citations"] = (
            aws_sdk_bedrock_runtime.types.citations_config.deserialize_json(
                data["citations"]
            )
        )
    return out
