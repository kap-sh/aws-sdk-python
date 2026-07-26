"""Generated from Smithy shape ``com.amazonaws.schemas#ExportSchemaRequest``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import capo_schemas.types.__string


class ExportSchemaRequest(TypedDict, closed=True):
    registry_name: "capo_schemas.types.__string.__string"
    """<p>The name of the registry.</p>"""
    schema_name: "capo_schemas.types.__string.__string"
    """<p>The name of the schema.</p>"""
    schema_version: NotRequired["capo_schemas.types.__string.__string"]
    """<p>Specifying this limits the results to only this schema version.</p>"""
    type: NotRequired["capo_schemas.types.__string.__string"]


# --- restJson1 ser/de ---
def serialize_json(value: ExportSchemaRequest) -> dict:
    out: dict = {}
    return out


def deserialize_json(data: dict) -> ExportSchemaRequest:
    out: ExportSchemaRequest = {}  # type: ignore[typeddict-item]
    return out
