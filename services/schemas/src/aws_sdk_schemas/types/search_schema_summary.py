"""Generated from Smithy shape ``com.amazonaws.schemas#SearchSchemaSummary``."""

from typing import TYPE_CHECKING, TypedDict

from typing_extensions import NotRequired

if TYPE_CHECKING:
    import aws_sdk_schemas.types.__list_of_search_schema_version_summary
    import aws_sdk_schemas.types.__string


class SearchSchemaSummary(TypedDict):
    registry_name: NotRequired["aws_sdk_schemas.types.__string.__string"]
    """<p>The name of the registry.</p>"""
    schema_arn: NotRequired["aws_sdk_schemas.types.__string.__string"]
    """<p>The ARN of the schema.</p>"""
    schema_name: NotRequired["aws_sdk_schemas.types.__string.__string"]
    """<p>The name of the schema.</p>"""
    schema_versions: NotRequired[
        "aws_sdk_schemas.types.__list_of_search_schema_version_summary.__listOfSearchSchemaVersionSummary"
    ]
    """<p>An array of schema version summaries.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: SearchSchemaSummary) -> dict:
    out: dict = {}
    if "registry_name" in value:
        out["RegistryName"] = value["registry_name"]
    if "schema_arn" in value:
        out["SchemaArn"] = value["schema_arn"]
    if "schema_name" in value:
        out["SchemaName"] = value["schema_name"]
    if "schema_versions" in value:
        import aws_sdk_schemas.types.__list_of_search_schema_version_summary

        out["SchemaVersions"] = (
            aws_sdk_schemas.types.__list_of_search_schema_version_summary.serialize_json(
                value["schema_versions"]
            )
        )
    return out


def deserialize_json(data: dict) -> SearchSchemaSummary:
    out: SearchSchemaSummary = {}  # type: ignore[typeddict-item]
    if "RegistryName" in data:
        out["registry_name"] = data["RegistryName"]
    if "SchemaArn" in data:
        out["schema_arn"] = data["SchemaArn"]
    if "SchemaName" in data:
        out["schema_name"] = data["SchemaName"]
    if "SchemaVersions" in data:
        import aws_sdk_schemas.types.__list_of_search_schema_version_summary

        out["schema_versions"] = (
            aws_sdk_schemas.types.__list_of_search_schema_version_summary.deserialize_json(
                data["SchemaVersions"]
            )
        )
    return out
