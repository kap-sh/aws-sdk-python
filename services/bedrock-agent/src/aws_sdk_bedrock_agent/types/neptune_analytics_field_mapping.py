"""Generated from Smithy shape ``com.amazonaws.bedrockagent#NeptuneAnalyticsFieldMapping``."""

from typing import TYPE_CHECKING, TypedDict

from aws_sdk_bedrock_agent.errors import DeserializationError

if TYPE_CHECKING:
    import aws_sdk_bedrock_agent.types.field_name


class NeptuneAnalyticsFieldMapping(TypedDict):
    text_field: "aws_sdk_bedrock_agent.types.field_name.FieldName"
    """<p>The name of the field in which Amazon Bedrock stores the raw text from your data. The text is split according to the chunking strategy you choose.</p>"""
    metadata_field: "aws_sdk_bedrock_agent.types.field_name.FieldName"
    """<p>The name of the field in which Amazon Bedrock stores metadata about the vector store.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: NeptuneAnalyticsFieldMapping) -> dict:
    out: dict = {}
    out["textField"] = value["text_field"]
    out["metadataField"] = value["metadata_field"]
    return out


def deserialize_json(data: dict) -> NeptuneAnalyticsFieldMapping:
    out: NeptuneAnalyticsFieldMapping = {}  # type: ignore[typeddict-item]
    if "textField" in data:
        out["text_field"] = data["textField"]
    else:
        raise DeserializationError("NeptuneAnalyticsFieldMapping.text_field required")
    if "metadataField" in data:
        out["metadata_field"] = data["metadataField"]
    else:
        raise DeserializationError(
            "NeptuneAnalyticsFieldMapping.metadata_field required"
        )
    return out
