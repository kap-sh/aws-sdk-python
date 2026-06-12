"""Generated from Smithy shape ``com.amazonaws.schemas#DeleteSchemaRequest``."""

from typing import TYPE_CHECKING, TypedDict

if TYPE_CHECKING:
    import aws_sdk_schemas.types.__string


class DeleteSchemaRequest(TypedDict):
    registry_name: "aws_sdk_schemas.types.__string.__string"
    """<p>The name of the registry.</p>"""
    schema_name: "aws_sdk_schemas.types.__string.__string"
    """<p>The name of the schema.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: DeleteSchemaRequest) -> dict:
    out: dict = {}
    return out


def deserialize_json(data: dict) -> DeleteSchemaRequest:
    out: DeleteSchemaRequest = {}  # type: ignore[typeddict-item]
    return out
