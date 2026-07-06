"""Generated from Smithy shape ``com.amazonaws.clouddirectory#CreateSchemaRequest``."""

from typing import TYPE_CHECKING

from typing_extensions import TypedDict

from aws_sdk_clouddirectory.errors import DeserializationError

if TYPE_CHECKING:
    import aws_sdk_clouddirectory.types.schema_name


class CreateSchemaRequest(TypedDict, closed=True):
    name: "aws_sdk_clouddirectory.types.schema_name.SchemaName"
    """<p>The name that is associated with the schema. This is unique to each account and in each region.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: CreateSchemaRequest) -> dict:
    out: dict = {}
    out["Name"] = value["name"]
    return out


def deserialize_json(data: dict) -> CreateSchemaRequest:
    out: CreateSchemaRequest = {}  # type: ignore[typeddict-item]
    if "Name" in data:
        out["name"] = data["Name"]
    else:
        raise DeserializationError("CreateSchemaRequest.name required")
    return out
