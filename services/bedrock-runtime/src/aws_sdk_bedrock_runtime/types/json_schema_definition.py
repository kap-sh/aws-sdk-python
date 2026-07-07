"""Generated from Smithy shape ``com.amazonaws.bedrockruntime#JsonSchemaDefinition``."""

from typing_extensions import NotRequired, TypedDict

from aws_sdk_bedrock_runtime.errors import DeserializationError


class JsonSchemaDefinition(TypedDict, closed=True):
    schema: "str"
    r"""<p> The JSON schema to constrain the model's output. For more information, see <a href=\"https://json-schema.org/understanding-json-schema/reference\">JSON Schema Reference</a>. </p>"""
    name: NotRequired["str"]
    """<p> The name of the JSON schema. </p>"""
    description: NotRequired["str"]
    """<p> A description of the JSON schema. </p>"""


# --- restJson1 ser/de ---
def serialize_json(value: JsonSchemaDefinition) -> dict:
    out: dict = {}
    out["schema"] = value["schema"]
    if "name" in value:
        out["name"] = value["name"]
    if "description" in value:
        out["description"] = value["description"]
    return out


def deserialize_json(data: dict) -> JsonSchemaDefinition:
    out: JsonSchemaDefinition = {}  # type: ignore[typeddict-item]
    if "schema" in data:
        out["schema"] = data["schema"]
    else:
        raise DeserializationError("JsonSchemaDefinition.schema required")
    if "name" in data:
        out["name"] = data["name"]
    if "description" in data:
        out["description"] = data["description"]
    return out
