"""Generated from Smithy shape ``com.amazonaws.dataexchange#SchemaChangeDetails``."""

from typing import TYPE_CHECKING, TypedDict

from typing_extensions import NotRequired

from aws_sdk_dataexchange.errors import DeserializationError

if TYPE_CHECKING:
    import aws_sdk_dataexchange.types.__string
    import aws_sdk_dataexchange.types.schema_change_type


class SchemaChangeDetails(TypedDict):
    name: "aws_sdk_dataexchange.types.__string.__string"
    """<p>Name of the changing field. This value can be up to 255 characters long.</p>"""
    type: "aws_sdk_dataexchange.types.schema_change_type.SchemaChangeType"
    """<p>Is the field being added, removed, or modified?</p>"""
    description: NotRequired["aws_sdk_dataexchange.types.__string.__string"]
    """<p>Description of what's changing about this field. This value can be up to 512 characters long.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: SchemaChangeDetails) -> dict:
    out: dict = {}
    out["Name"] = value["name"]
    out["Type"] = value["type"]
    if "description" in value:
        out["Description"] = value["description"]
    return out


def deserialize_json(data: dict) -> SchemaChangeDetails:
    out: SchemaChangeDetails = {}  # type: ignore[typeddict-item]
    if "Name" in data:
        out["name"] = data["Name"]
    else:
        raise DeserializationError("SchemaChangeDetails.name required")
    if "Type" in data:
        out["type"] = data["Type"]
    else:
        raise DeserializationError("SchemaChangeDetails.type required")
    if "Description" in data:
        out["description"] = data["Description"]
    return out
