"""Generated from Smithy shape ``com.amazonaws.bedrockagent#MetadataAttributeValue``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

from aws_sdk_bedrock_agent.errors import DeserializationError

if TYPE_CHECKING:
    import aws_sdk_bedrock_agent.types.metadata_value_type
    import aws_sdk_bedrock_agent.types.number_value
    import aws_sdk_bedrock_agent.types.string_list_value
    import aws_sdk_bedrock_agent.types.string_value


class MetadataAttributeValue(TypedDict, closed=True):
    type: "aws_sdk_bedrock_agent.types.metadata_value_type.MetadataValueType"
    """<p>The type of the metadata attribute.</p>"""
    number_value: NotRequired["aws_sdk_bedrock_agent.types.number_value.NumberValue"]
    """<p>The value of the numeric metadata attribute.</p>"""
    boolean_value: NotRequired["bool"]
    """<p>The value of the Boolean metadata attribute.</p>"""
    string_value: NotRequired["aws_sdk_bedrock_agent.types.string_value.StringValue"]
    """<p>The value of the string metadata attribute.</p>"""
    string_list_value: NotRequired[
        "aws_sdk_bedrock_agent.types.string_list_value.StringListValue"
    ]
    """<p>An array of strings that define the value of the metadata attribute.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: MetadataAttributeValue) -> dict:
    out: dict = {}
    import aws_sdk_bedrock_agent.types.metadata_value_type

    out["type"] = aws_sdk_bedrock_agent.types.metadata_value_type.serialize_json(
        value["type"]
    )
    if "number_value" in value:
        out["numberValue"] = value["number_value"]
    if "boolean_value" in value:
        out["booleanValue"] = value["boolean_value"]
    if "string_value" in value:
        out["stringValue"] = value["string_value"]
    if "string_list_value" in value:
        import aws_sdk_bedrock_agent.types.string_list_value

        out["stringListValue"] = (
            aws_sdk_bedrock_agent.types.string_list_value.serialize_json(
                value["string_list_value"]
            )
        )
    return out


def deserialize_json(data: dict) -> MetadataAttributeValue:
    out: MetadataAttributeValue = {}  # type: ignore[typeddict-item]
    if "type" in data:
        import aws_sdk_bedrock_agent.types.metadata_value_type

        out["type"] = aws_sdk_bedrock_agent.types.metadata_value_type.deserialize_json(
            data["type"]
        )
    else:
        raise DeserializationError("MetadataAttributeValue.type required")
    if "numberValue" in data:
        out["number_value"] = data["numberValue"]
    if "booleanValue" in data:
        out["boolean_value"] = data["booleanValue"]
    if "stringValue" in data:
        out["string_value"] = data["stringValue"]
    if "stringListValue" in data:
        import aws_sdk_bedrock_agent.types.string_list_value

        out["string_list_value"] = (
            aws_sdk_bedrock_agent.types.string_list_value.deserialize_json(
                data["stringListValue"]
            )
        )
    return out
