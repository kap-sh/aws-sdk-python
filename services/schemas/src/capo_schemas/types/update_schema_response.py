"""Generated from Smithy shape ``com.amazonaws.schemas#UpdateSchemaResponse``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import capo_schemas.types.__string
    import capo_schemas.types.__timestamp_iso8601
    import capo_schemas.types.tags


class UpdateSchemaResponse(TypedDict, closed=True):
    description: NotRequired["capo_schemas.types.__string.__string"]
    """<p>The description of the schema.</p>"""
    last_modified: NotRequired[
        "capo_schemas.types.__timestamp_iso8601.__timestampIso8601"
    ]
    """<p>The date and time that schema was modified.</p>"""
    schema_arn: NotRequired["capo_schemas.types.__string.__string"]
    """<p>The ARN of the schema.</p>"""
    schema_name: NotRequired["capo_schemas.types.__string.__string"]
    """<p>The name of the schema.</p>"""
    schema_version: NotRequired["capo_schemas.types.__string.__string"]
    """<p>The version number of the schema</p>"""
    tags: NotRequired["capo_schemas.types.tags.Tags"]
    type: NotRequired["capo_schemas.types.__string.__string"]
    """<p>The type of the schema.</p>"""
    version_created_date: NotRequired[
        "capo_schemas.types.__timestamp_iso8601.__timestampIso8601"
    ]
    """<p>The date the schema version was created.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: UpdateSchemaResponse) -> dict:
    out: dict = {}
    if "description" in value:
        out["Description"] = value["description"]
    if "last_modified" in value:
        import capo_schemas.types.__timestamp_iso8601

        out["LastModified"] = capo_schemas.types.__timestamp_iso8601.serialize_json(
            value["last_modified"]
        )
    if "schema_arn" in value:
        out["SchemaArn"] = value["schema_arn"]
    if "schema_name" in value:
        out["SchemaName"] = value["schema_name"]
    if "schema_version" in value:
        out["SchemaVersion"] = value["schema_version"]
    if "tags" in value:
        import capo_schemas.types.tags

        out["tags"] = capo_schemas.types.tags.serialize_json(value["tags"])
    if "type" in value:
        out["Type"] = value["type"]
    if "version_created_date" in value:
        import capo_schemas.types.__timestamp_iso8601

        out["VersionCreatedDate"] = (
            capo_schemas.types.__timestamp_iso8601.serialize_json(
                value["version_created_date"]
            )
        )
    return out


def deserialize_json(data: dict) -> UpdateSchemaResponse:
    out: UpdateSchemaResponse = {}  # type: ignore[typeddict-item]
    if "Description" in data:
        out["description"] = data["Description"]
    if "LastModified" in data:
        import capo_schemas.types.__timestamp_iso8601

        out["last_modified"] = capo_schemas.types.__timestamp_iso8601.deserialize_json(
            data["LastModified"]
        )
    if "SchemaArn" in data:
        out["schema_arn"] = data["SchemaArn"]
    if "SchemaName" in data:
        out["schema_name"] = data["SchemaName"]
    if "SchemaVersion" in data:
        out["schema_version"] = data["SchemaVersion"]
    if "tags" in data:
        import capo_schemas.types.tags

        out["tags"] = capo_schemas.types.tags.deserialize_json(data["tags"])
    if "Type" in data:
        out["type"] = data["Type"]
    if "VersionCreatedDate" in data:
        import capo_schemas.types.__timestamp_iso8601

        out["version_created_date"] = (
            capo_schemas.types.__timestamp_iso8601.deserialize_json(
                data["VersionCreatedDate"]
            )
        )
    return out
