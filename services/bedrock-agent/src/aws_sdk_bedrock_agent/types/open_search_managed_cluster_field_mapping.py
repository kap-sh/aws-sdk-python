"""Generated from Smithy shape ``com.amazonaws.bedrockagent#OpenSearchManagedClusterFieldMapping``."""

from typing import TYPE_CHECKING, TypedDict

from aws_sdk_bedrock_agent.errors import DeserializationError

if TYPE_CHECKING:
    import aws_sdk_bedrock_agent.types.field_name


class OpenSearchManagedClusterFieldMapping(TypedDict):
    vector_field: "aws_sdk_bedrock_agent.types.field_name.FieldName"
    """<p>The name of the field in which Amazon Bedrock stores the vector embeddings for your data sources.</p>"""
    text_field: "aws_sdk_bedrock_agent.types.field_name.FieldName"
    """<p>The name of the field in which Amazon Bedrock stores the raw text from your data. The text is split according to the chunking strategy you choose.</p>"""
    metadata_field: "aws_sdk_bedrock_agent.types.field_name.FieldName"
    """<p>The name of the field in which Amazon Bedrock stores metadata about the vector store.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: OpenSearchManagedClusterFieldMapping) -> dict:
    out: dict = {}
    out["vectorField"] = value["vector_field"]
    out["textField"] = value["text_field"]
    out["metadataField"] = value["metadata_field"]
    return out


def deserialize_json(data: dict) -> OpenSearchManagedClusterFieldMapping:
    out: OpenSearchManagedClusterFieldMapping = {}  # type: ignore[typeddict-item]
    if "vectorField" in data:
        out["vector_field"] = data["vectorField"]
    else:
        raise DeserializationError(
            "OpenSearchManagedClusterFieldMapping.vector_field required"
        )
    if "textField" in data:
        out["text_field"] = data["textField"]
    else:
        raise DeserializationError(
            "OpenSearchManagedClusterFieldMapping.text_field required"
        )
    if "metadataField" in data:
        out["metadata_field"] = data["metadataField"]
    else:
        raise DeserializationError(
            "OpenSearchManagedClusterFieldMapping.metadata_field required"
        )
    return out
