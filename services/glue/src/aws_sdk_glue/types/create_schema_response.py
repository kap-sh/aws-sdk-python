"""Generated from Smithy shape ``com.amazonaws.glue#CreateSchemaResponse``."""

from typing import TYPE_CHECKING, TypedDict

from typing_extensions import NotRequired

if TYPE_CHECKING:
    import aws_sdk_glue.types.compatibility
    import aws_sdk_glue.types.data_format
    import aws_sdk_glue.types.description_string
    import aws_sdk_glue.types.glue_resource_arn
    import aws_sdk_glue.types.schema_checkpoint_number
    import aws_sdk_glue.types.schema_registry_name_string
    import aws_sdk_glue.types.schema_status
    import aws_sdk_glue.types.schema_version_id_string
    import aws_sdk_glue.types.schema_version_status
    import aws_sdk_glue.types.tags_map
    import aws_sdk_glue.types.version_long_number


class CreateSchemaResponse(TypedDict):
    registry_name: NotRequired[
        "aws_sdk_glue.types.schema_registry_name_string.SchemaRegistryNameString"
    ]
    """<p>The name of the registry.</p>"""
    registry_arn: NotRequired["aws_sdk_glue.types.glue_resource_arn.GlueResourceArn"]
    """<p>The Amazon Resource Name (ARN) of the registry.</p>"""
    schema_name: NotRequired[
        "aws_sdk_glue.types.schema_registry_name_string.SchemaRegistryNameString"
    ]
    """<p>The name of the schema.</p>"""
    schema_arn: NotRequired["aws_sdk_glue.types.glue_resource_arn.GlueResourceArn"]
    """<p>The Amazon Resource Name (ARN) of the schema.</p>"""
    description: NotRequired["aws_sdk_glue.types.description_string.DescriptionString"]
    """<p>A description of the schema if specified when created.</p>"""
    data_format: NotRequired["aws_sdk_glue.types.data_format.DataFormat"]
    """<p>The data format of the schema definition. Currently <code>AVRO</code>, <code>JSON</code> and <code>PROTOBUF</code> are supported.</p>"""
    compatibility: NotRequired["aws_sdk_glue.types.compatibility.Compatibility"]
    """<p>The schema compatibility mode.</p>"""
    schema_checkpoint: NotRequired[
        "aws_sdk_glue.types.schema_checkpoint_number.SchemaCheckpointNumber"
    ]
    """<p>The version number of the checkpoint (the last time the compatibility mode was changed).</p>"""
    latest_schema_version: NotRequired[
        "aws_sdk_glue.types.version_long_number.VersionLongNumber"
    ]
    """<p>The latest version of the schema associated with the returned schema definition.</p>"""
    next_schema_version: NotRequired[
        "aws_sdk_glue.types.version_long_number.VersionLongNumber"
    ]
    """<p>The next version of the schema associated with the returned schema definition.</p>"""
    schema_status: NotRequired["aws_sdk_glue.types.schema_status.SchemaStatus"]
    """<p>The status of the schema. </p>"""
    tags: NotRequired["aws_sdk_glue.types.tags_map.TagsMap"]
    """<p>The tags for the schema.</p>"""
    schema_version_id: NotRequired[
        "aws_sdk_glue.types.schema_version_id_string.SchemaVersionIdString"
    ]
    """<p>The unique identifier of the first schema version.</p>"""
    schema_version_status: NotRequired[
        "aws_sdk_glue.types.schema_version_status.SchemaVersionStatus"
    ]
    """<p>The status of the first schema version created.</p>"""


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: CreateSchemaResponse) -> dict:
    out: dict = {}
    if "registry_name" in value:
        out["RegistryName"] = value["registry_name"]
    if "registry_arn" in value:
        out["RegistryArn"] = value["registry_arn"]
    if "schema_name" in value:
        out["SchemaName"] = value["schema_name"]
    if "schema_arn" in value:
        out["SchemaArn"] = value["schema_arn"]
    if "description" in value:
        out["Description"] = value["description"]
    if "data_format" in value:
        import aws_sdk_glue.types.data_format

        out["DataFormat"] = aws_sdk_glue.types.data_format.serialize_aws_json_1_1(
            value["data_format"]
        )
    if "compatibility" in value:
        import aws_sdk_glue.types.compatibility

        out["Compatibility"] = aws_sdk_glue.types.compatibility.serialize_aws_json_1_1(
            value["compatibility"]
        )
    if "schema_checkpoint" in value:
        out["SchemaCheckpoint"] = value["schema_checkpoint"]
    if "latest_schema_version" in value:
        out["LatestSchemaVersion"] = value["latest_schema_version"]
    if "next_schema_version" in value:
        out["NextSchemaVersion"] = value["next_schema_version"]
    if "schema_status" in value:
        import aws_sdk_glue.types.schema_status

        out["SchemaStatus"] = aws_sdk_glue.types.schema_status.serialize_aws_json_1_1(
            value["schema_status"]
        )
    if "tags" in value:
        import aws_sdk_glue.types.tags_map

        out["Tags"] = aws_sdk_glue.types.tags_map.serialize_aws_json_1_1(value["tags"])
    if "schema_version_id" in value:
        out["SchemaVersionId"] = value["schema_version_id"]
    if "schema_version_status" in value:
        import aws_sdk_glue.types.schema_version_status

        out["SchemaVersionStatus"] = (
            aws_sdk_glue.types.schema_version_status.serialize_aws_json_1_1(
                value["schema_version_status"]
            )
        )
    return out


def deserialize_aws_json_1_1(data: dict) -> CreateSchemaResponse:
    out: CreateSchemaResponse = {}  # type: ignore[typeddict-item]
    if "RegistryName" in data:
        out["registry_name"] = data["RegistryName"]
    if "RegistryArn" in data:
        out["registry_arn"] = data["RegistryArn"]
    if "SchemaName" in data:
        out["schema_name"] = data["SchemaName"]
    if "SchemaArn" in data:
        out["schema_arn"] = data["SchemaArn"]
    if "Description" in data:
        out["description"] = data["Description"]
    if "DataFormat" in data:
        import aws_sdk_glue.types.data_format

        out["data_format"] = aws_sdk_glue.types.data_format.deserialize_aws_json_1_1(
            data["DataFormat"]
        )
    if "Compatibility" in data:
        import aws_sdk_glue.types.compatibility

        out["compatibility"] = (
            aws_sdk_glue.types.compatibility.deserialize_aws_json_1_1(
                data["Compatibility"]
            )
        )
    if "SchemaCheckpoint" in data:
        out["schema_checkpoint"] = data["SchemaCheckpoint"]
    if "LatestSchemaVersion" in data:
        out["latest_schema_version"] = data["LatestSchemaVersion"]
    if "NextSchemaVersion" in data:
        out["next_schema_version"] = data["NextSchemaVersion"]
    if "SchemaStatus" in data:
        import aws_sdk_glue.types.schema_status

        out["schema_status"] = (
            aws_sdk_glue.types.schema_status.deserialize_aws_json_1_1(
                data["SchemaStatus"]
            )
        )
    if "Tags" in data:
        import aws_sdk_glue.types.tags_map

        out["tags"] = aws_sdk_glue.types.tags_map.deserialize_aws_json_1_1(data["Tags"])
    if "SchemaVersionId" in data:
        out["schema_version_id"] = data["SchemaVersionId"]
    if "SchemaVersionStatus" in data:
        import aws_sdk_glue.types.schema_version_status

        out["schema_version_status"] = (
            aws_sdk_glue.types.schema_version_status.deserialize_aws_json_1_1(
                data["SchemaVersionStatus"]
            )
        )
    return out
