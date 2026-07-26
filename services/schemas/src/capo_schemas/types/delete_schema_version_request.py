"""Generated from Smithy shape ``com.amazonaws.schemas#DeleteSchemaVersionRequest``."""

from typing import TYPE_CHECKING

from typing_extensions import TypedDict

if TYPE_CHECKING:
    import capo_schemas.types.__string


class DeleteSchemaVersionRequest(TypedDict, closed=True):
    registry_name: "capo_schemas.types.__string.__string"
    """<p>The name of the registry.</p>"""
    schema_name: "capo_schemas.types.__string.__string"
    """<p>The name of the schema.</p>"""
    schema_version: "capo_schemas.types.__string.__string"
    """The version number of the schema"""


# --- restJson1 ser/de ---
def serialize_json(value: DeleteSchemaVersionRequest) -> dict:
    out: dict = {}
    return out


def deserialize_json(data: dict) -> DeleteSchemaVersionRequest:
    out: DeleteSchemaVersionRequest = {}  # type: ignore[typeddict-item]
    return out
