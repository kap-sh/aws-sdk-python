"""Generated from Smithy shape ``com.amazonaws.glue#KeySchemaElement``."""

from typing import TYPE_CHECKING

from typing_extensions import TypedDict

from capo_glue.errors import DeserializationError

if TYPE_CHECKING:
    import capo_glue.types.column_type_string
    import capo_glue.types.name_string


class KeySchemaElement(TypedDict, closed=True):
    name: "capo_glue.types.name_string.NameString"
    """<p>The name of a partition key.</p>"""
    type: "capo_glue.types.column_type_string.ColumnTypeString"
    """<p>The type of a partition key.</p>"""


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: KeySchemaElement) -> dict:
    out: dict = {}
    out["Name"] = value["name"]
    out["Type"] = value["type"]
    return out


def deserialize_aws_json_1_1(data: dict) -> KeySchemaElement:
    out: KeySchemaElement = {}  # type: ignore[typeddict-item]
    if "Name" in data:
        out["name"] = data["Name"]
    else:
        raise DeserializationError("KeySchemaElement.name required")
    if "Type" in data:
        out["type"] = data["Type"]
    else:
        raise DeserializationError("KeySchemaElement.type required")
    return out
