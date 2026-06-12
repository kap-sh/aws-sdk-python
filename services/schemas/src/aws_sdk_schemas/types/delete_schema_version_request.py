"""Generated from Smithy shape ``com.amazonaws.schemas#DeleteSchemaVersionRequest``."""

from typing import TYPE_CHECKING, TypedDict

if TYPE_CHECKING:
    import aws_sdk_schemas.types.__string


class DeleteSchemaVersionRequest(TypedDict):
    registry_name: "aws_sdk_schemas.types.__string.__string"
    """<p>The name of the registry.</p>"""
    schema_name: "aws_sdk_schemas.types.__string.__string"
    """<p>The name of the schema.</p>"""
    schema_version: "aws_sdk_schemas.types.__string.__string"
    """The version number of the schema"""


# --- restJson1 ser/de ---
def serialize_json(value: DeleteSchemaVersionRequest) -> dict:
    out: dict = {}
    return out


def deserialize_json(data: dict) -> DeleteSchemaVersionRequest:
    out: DeleteSchemaVersionRequest = {}  # type: ignore[typeddict-item]
    return out
