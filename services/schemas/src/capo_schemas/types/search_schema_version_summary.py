"""Generated from Smithy shape ``com.amazonaws.schemas#SearchSchemaVersionSummary``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import capo_schemas.types.__string
    import capo_schemas.types.__timestamp_iso8601
    import capo_schemas.types.type


class SearchSchemaVersionSummary(TypedDict, closed=True):
    created_date: NotRequired[
        "capo_schemas.types.__timestamp_iso8601.__timestampIso8601"
    ]
    """<p>The date the schema version was created.</p>"""
    schema_version: NotRequired["capo_schemas.types.__string.__string"]
    """<p>The version number of the schema</p>"""
    type: NotRequired["capo_schemas.types.type.Type"]
    """<p>The type of schema.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: SearchSchemaVersionSummary) -> dict:
    out: dict = {}
    if "created_date" in value:
        import capo_schemas.types.__timestamp_iso8601

        out["CreatedDate"] = capo_schemas.types.__timestamp_iso8601.serialize_json(
            value["created_date"]
        )
    if "schema_version" in value:
        out["SchemaVersion"] = value["schema_version"]
    if "type" in value:
        import capo_schemas.types.type

        out["Type"] = capo_schemas.types.type.serialize_json(value["type"])
    return out


def deserialize_json(data: dict) -> SearchSchemaVersionSummary:
    out: SearchSchemaVersionSummary = {}  # type: ignore[typeddict-item]
    if "CreatedDate" in data:
        import capo_schemas.types.__timestamp_iso8601

        out["created_date"] = capo_schemas.types.__timestamp_iso8601.deserialize_json(
            data["CreatedDate"]
        )
    if "SchemaVersion" in data:
        out["schema_version"] = data["SchemaVersion"]
    if "Type" in data:
        import capo_schemas.types.type

        out["type"] = capo_schemas.types.type.deserialize_json(data["Type"])
    return out
