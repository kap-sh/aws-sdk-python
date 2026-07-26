"""Generated from Smithy shape ``com.amazonaws.schemas#SchemaVersionSummary``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import capo_schemas.types.__string
    import capo_schemas.types.type


class SchemaVersionSummary(TypedDict, closed=True):
    schema_arn: NotRequired["capo_schemas.types.__string.__string"]
    """<p>The ARN of the schema version.</p>"""
    schema_name: NotRequired["capo_schemas.types.__string.__string"]
    """<p>The name of the schema.</p>"""
    schema_version: NotRequired["capo_schemas.types.__string.__string"]
    """<p>The version number of the schema.</p>"""
    type: NotRequired["capo_schemas.types.type.Type"]
    """<p>The type of schema.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: SchemaVersionSummary) -> dict:
    out: dict = {}
    if "schema_arn" in value:
        out["SchemaArn"] = value["schema_arn"]
    if "schema_name" in value:
        out["SchemaName"] = value["schema_name"]
    if "schema_version" in value:
        out["SchemaVersion"] = value["schema_version"]
    if "type" in value:
        import capo_schemas.types.type

        out["Type"] = capo_schemas.types.type.serialize_json(value["type"])
    return out


def deserialize_json(data: dict) -> SchemaVersionSummary:
    out: SchemaVersionSummary = {}  # type: ignore[typeddict-item]
    if "SchemaArn" in data:
        out["schema_arn"] = data["SchemaArn"]
    if "SchemaName" in data:
        out["schema_name"] = data["SchemaName"]
    if "SchemaVersion" in data:
        out["schema_version"] = data["SchemaVersion"]
    if "Type" in data:
        import capo_schemas.types.type

        out["type"] = capo_schemas.types.type.deserialize_json(data["Type"])
    return out
