"""Generated from Smithy shape ``com.amazonaws.novaact#ToolInputSchema``."""

from typing import TYPE_CHECKING, TypeAlias, TypedDict

from aws_sdk_nova_act.errors import DeserializationError, SerializationError

if TYPE_CHECKING:
    import aws_sdk_nova_act.types.tool_input_schema_document


class _ToolInputSchema_json(TypedDict):
    json: "aws_sdk_nova_act.types.tool_input_schema_document.ToolInputSchemaDocument"


ToolInputSchema: TypeAlias = _ToolInputSchema_json


# --- restJson1 ser/de ---
def serialize_json(value: ToolInputSchema) -> dict:
    if "json" in value:
        return {"json": value["json"]}
    else:
        raise SerializationError("ToolInputSchema: no variant present")


def deserialize_json(data: dict) -> ToolInputSchema:
    if "json" in data:
        return {"json": data["json"]}
    else:
        raise DeserializationError("ToolInputSchema: no recognized variant key")
