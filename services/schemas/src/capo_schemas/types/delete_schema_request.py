"""Generated from Smithy shape ``com.amazonaws.schemas#DeleteSchemaRequest``."""

from typing import TYPE_CHECKING

from typing_extensions import TypedDict

if TYPE_CHECKING:
    import capo_schemas.types.__string


class DeleteSchemaRequest(TypedDict, closed=True):
    registry_name: "capo_schemas.types.__string.__string"
    """<p>The name of the registry.</p>"""
    schema_name: "capo_schemas.types.__string.__string"
    """<p>The name of the schema.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: DeleteSchemaRequest) -> dict:
    out: dict = {}
    return out


def deserialize_json(data: dict) -> DeleteSchemaRequest:
    out: DeleteSchemaRequest = {}  # type: ignore[typeddict-item]
    return out
