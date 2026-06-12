"""Generated from Smithy shape ``com.amazonaws.schemas#CreateSchemaResponse``."""

from typing import TYPE_CHECKING, TypedDict

from typing_extensions import NotRequired

if TYPE_CHECKING:
    import aws_sdk_schemas.types.__string
    import aws_sdk_schemas.types.__timestamp_iso8601
    import aws_sdk_schemas.types.tags


class CreateSchemaResponse(TypedDict):
    description: NotRequired["aws_sdk_schemas.types.__string.__string"]
    """<p>The description of the schema.</p>"""
    last_modified: NotRequired[
        "aws_sdk_schemas.types.__timestamp_iso8601.__timestampIso8601"
    ]
    """<p>The date and time that schema was modified.</p>"""
    schema_arn: NotRequired["aws_sdk_schemas.types.__string.__string"]
    """<p>The ARN of the schema.</p>"""
    schema_name: NotRequired["aws_sdk_schemas.types.__string.__string"]
    """<p>The name of the schema.</p>"""
    schema_version: NotRequired["aws_sdk_schemas.types.__string.__string"]
    """<p>The version number of the schema</p>"""
    tags: NotRequired["aws_sdk_schemas.types.tags.Tags"]
    type: NotRequired["aws_sdk_schemas.types.__string.__string"]
    """<p>The type of the schema.</p>"""
    version_created_date: NotRequired[
        "aws_sdk_schemas.types.__timestamp_iso8601.__timestampIso8601"
    ]
    """<p>The date the schema version was created.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: CreateSchemaResponse) -> dict:
    out: dict = {}
    if "description" in value:
        out["Description"] = value["description"]
    if "last_modified" in value:
        import aws_sdk_schemas.types.__timestamp_iso8601

        out["LastModified"] = aws_sdk_schemas.types.__timestamp_iso8601.serialize_json(
            value["last_modified"]
        )
    if "schema_arn" in value:
        out["SchemaArn"] = value["schema_arn"]
    if "schema_name" in value:
        out["SchemaName"] = value["schema_name"]
    if "schema_version" in value:
        out["SchemaVersion"] = value["schema_version"]
    if "tags" in value:
        import aws_sdk_schemas.types.tags

        out["tags"] = aws_sdk_schemas.types.tags.serialize_json(value["tags"])
    if "type" in value:
        out["Type"] = value["type"]
    if "version_created_date" in value:
        import aws_sdk_schemas.types.__timestamp_iso8601

        out["VersionCreatedDate"] = (
            aws_sdk_schemas.types.__timestamp_iso8601.serialize_json(
                value["version_created_date"]
            )
        )
    return out


def deserialize_json(data: dict) -> CreateSchemaResponse:
    out: CreateSchemaResponse = {}  # type: ignore[typeddict-item]
    if "Description" in data:
        out["description"] = data["Description"]
    if "LastModified" in data:
        import aws_sdk_schemas.types.__timestamp_iso8601

        out["last_modified"] = (
            aws_sdk_schemas.types.__timestamp_iso8601.deserialize_json(
                data["LastModified"]
            )
        )
    if "SchemaArn" in data:
        out["schema_arn"] = data["SchemaArn"]
    if "SchemaName" in data:
        out["schema_name"] = data["SchemaName"]
    if "SchemaVersion" in data:
        out["schema_version"] = data["SchemaVersion"]
    if "tags" in data:
        import aws_sdk_schemas.types.tags

        out["tags"] = aws_sdk_schemas.types.tags.deserialize_json(data["tags"])
    if "Type" in data:
        out["type"] = data["Type"]
    if "VersionCreatedDate" in data:
        import aws_sdk_schemas.types.__timestamp_iso8601

        out["version_created_date"] = (
            aws_sdk_schemas.types.__timestamp_iso8601.deserialize_json(
                data["VersionCreatedDate"]
            )
        )
    return out
