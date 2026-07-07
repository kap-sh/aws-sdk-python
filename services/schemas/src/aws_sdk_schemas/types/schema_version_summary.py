"""Generated from Smithy shape ``com.amazonaws.schemas#SchemaVersionSummary``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import aws_sdk_schemas.types.__string
    import aws_sdk_schemas.types.type


class SchemaVersionSummary(TypedDict, closed=True):
    schema_arn: NotRequired["aws_sdk_schemas.types.__string.__string"]
    """<p>The ARN of the schema version.</p>"""
    schema_name: NotRequired["aws_sdk_schemas.types.__string.__string"]
    """<p>The name of the schema.</p>"""
    schema_version: NotRequired["aws_sdk_schemas.types.__string.__string"]
    """<p>The version number of the schema.</p>"""
    type: NotRequired["aws_sdk_schemas.types.type.Type"]
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
        import aws_sdk_schemas.types.type

        out["Type"] = aws_sdk_schemas.types.type.serialize_json(value["type"])
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
        import aws_sdk_schemas.types.type

        out["type"] = aws_sdk_schemas.types.type.deserialize_json(data["Type"])
    return out
