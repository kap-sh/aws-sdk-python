"""Generated from Smithy shape ``com.amazonaws.qbusiness#CustomPluginConfiguration``."""

from typing import TYPE_CHECKING, TypedDict
from typing_extensions import NotRequired
from aws_sdk_qbusiness.errors import DeserializationError
if TYPE_CHECKING:
    import aws_sdk_qbusiness.types.api_schema
    import aws_sdk_qbusiness.types.api_schema_type
    import aws_sdk_qbusiness.types.plugin_description

class CustomPluginConfiguration(TypedDict):
    description: "aws_sdk_qbusiness.types.plugin_description.PluginDescription"
    """<p>A description for your custom plugin configuration.</p>"""
    api_schema_type: "aws_sdk_qbusiness.types.api_schema_type.APISchemaType"
    """<p>The type of OpenAPI schema to use.</p>"""
    api_schema: NotRequired["aws_sdk_qbusiness.types.api_schema.APISchema"]
    """<p>Contains either details about the S3 object containing the OpenAPI schema for the action group or the JSON or YAML-formatted payload defining the schema.</p>"""

# --- restJson1 ser/de ---
def serialize_json(value: CustomPluginConfiguration) -> dict:
    out: dict = {}
    out["description"] = value["description"]
    import aws_sdk_qbusiness.types.api_schema_type
    out["apiSchemaType"] = aws_sdk_qbusiness.types.api_schema_type.serialize_json(value["api_schema_type"])
    if "api_schema" in value:
        import aws_sdk_qbusiness.types.api_schema
        out["apiSchema"] = aws_sdk_qbusiness.types.api_schema.serialize_json(value["api_schema"])
    return out


def deserialize_json(data: dict) -> CustomPluginConfiguration:
    out: CustomPluginConfiguration = {}  # type: ignore[typeddict-item]
    if "description" in data:
        out["description"] = data["description"]
    else:
        raise DeserializationError("CustomPluginConfiguration.description required")
    if "apiSchemaType" in data:
        import aws_sdk_qbusiness.types.api_schema_type
        out["api_schema_type"] = aws_sdk_qbusiness.types.api_schema_type.deserialize_json(data["apiSchemaType"])
    else:
        raise DeserializationError("CustomPluginConfiguration.api_schema_type required")
    if "apiSchema" in data:
        import aws_sdk_qbusiness.types.api_schema
        out["api_schema"] = aws_sdk_qbusiness.types.api_schema.deserialize_json(data["apiSchema"])
    return out