"""Generated from Smithy shape ``com.amazonaws.glue#RemoveSchemaVersionMetadataResponse``."""

from typing import TYPE_CHECKING, TypedDict

from typing_extensions import NotRequired

if TYPE_CHECKING:
    import aws_sdk_glue.types.glue_resource_arn
    import aws_sdk_glue.types.latest_schema_version_boolean
    import aws_sdk_glue.types.metadata_key_string
    import aws_sdk_glue.types.metadata_value_string
    import aws_sdk_glue.types.schema_registry_name_string
    import aws_sdk_glue.types.schema_version_id_string
    import aws_sdk_glue.types.version_long_number


class RemoveSchemaVersionMetadataResponse(TypedDict):
    schema_arn: NotRequired["aws_sdk_glue.types.glue_resource_arn.GlueResourceArn"]
    """<p>The Amazon Resource Name (ARN) of the schema.</p>"""
    schema_name: NotRequired[
        "aws_sdk_glue.types.schema_registry_name_string.SchemaRegistryNameString"
    ]
    """<p>The name of the schema.</p>"""
    registry_name: NotRequired[
        "aws_sdk_glue.types.schema_registry_name_string.SchemaRegistryNameString"
    ]
    """<p>The name of the registry.</p>"""
    latest_version: (
        "aws_sdk_glue.types.latest_schema_version_boolean.LatestSchemaVersionBoolean"
    )
    """<p>The latest version of the schema.</p>"""
    version_number: NotRequired[
        "aws_sdk_glue.types.version_long_number.VersionLongNumber"
    ]
    """<p>The version number of the schema.</p>"""
    schema_version_id: NotRequired[
        "aws_sdk_glue.types.schema_version_id_string.SchemaVersionIdString"
    ]
    """<p>The version ID for the schema version.</p>"""
    metadata_key: NotRequired[
        "aws_sdk_glue.types.metadata_key_string.MetadataKeyString"
    ]
    """<p>The metadata key.</p>"""
    metadata_value: NotRequired[
        "aws_sdk_glue.types.metadata_value_string.MetadataValueString"
    ]
    """<p>The value of the metadata key.</p>"""


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: RemoveSchemaVersionMetadataResponse) -> dict:
    out: dict = {}
    if "schema_arn" in value:
        out["SchemaArn"] = value["schema_arn"]
    if "schema_name" in value:
        out["SchemaName"] = value["schema_name"]
    if "registry_name" in value:
        out["RegistryName"] = value["registry_name"]
    out["LatestVersion"] = value.get("latest_version", False)
    if "version_number" in value:
        out["VersionNumber"] = value["version_number"]
    if "schema_version_id" in value:
        out["SchemaVersionId"] = value["schema_version_id"]
    if "metadata_key" in value:
        out["MetadataKey"] = value["metadata_key"]
    if "metadata_value" in value:
        out["MetadataValue"] = value["metadata_value"]
    return out


def deserialize_aws_json_1_1(data: dict) -> RemoveSchemaVersionMetadataResponse:
    out: RemoveSchemaVersionMetadataResponse = {}  # type: ignore[typeddict-item]
    if "SchemaArn" in data:
        out["schema_arn"] = data["SchemaArn"]
    if "SchemaName" in data:
        out["schema_name"] = data["SchemaName"]
    if "RegistryName" in data:
        out["registry_name"] = data["RegistryName"]
    if "LatestVersion" in data:
        out["latest_version"] = data["LatestVersion"]
    else:
        out["latest_version"] = False
    if "VersionNumber" in data:
        out["version_number"] = data["VersionNumber"]
    if "SchemaVersionId" in data:
        out["schema_version_id"] = data["SchemaVersionId"]
    if "MetadataKey" in data:
        out["metadata_key"] = data["MetadataKey"]
    if "MetadataValue" in data:
        out["metadata_value"] = data["MetadataValue"]
    return out
