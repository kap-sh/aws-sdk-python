"""Generated from Smithy shape ``com.amazonaws.glue#SchemaListItem``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import aws_sdk_glue.types.created_timestamp
    import aws_sdk_glue.types.description_string
    import aws_sdk_glue.types.glue_resource_arn
    import aws_sdk_glue.types.schema_registry_name_string
    import aws_sdk_glue.types.schema_status
    import aws_sdk_glue.types.updated_timestamp


class SchemaListItem(TypedDict, closed=True):
    registry_name: NotRequired[
        "aws_sdk_glue.types.schema_registry_name_string.SchemaRegistryNameString"
    ]
    """<p>the name of the registry where the schema resides.</p>"""
    schema_name: NotRequired[
        "aws_sdk_glue.types.schema_registry_name_string.SchemaRegistryNameString"
    ]
    """<p>The name of the schema.</p>"""
    schema_arn: NotRequired["aws_sdk_glue.types.glue_resource_arn.GlueResourceArn"]
    """<p>The Amazon Resource Name (ARN) for the schema.</p>"""
    description: NotRequired["aws_sdk_glue.types.description_string.DescriptionString"]
    """<p>A description for the schema.</p>"""
    schema_status: NotRequired["aws_sdk_glue.types.schema_status.SchemaStatus"]
    """<p>The status of the schema.</p>"""
    created_time: NotRequired["aws_sdk_glue.types.created_timestamp.CreatedTimestamp"]
    """<p>The date and time that a schema was created.</p>"""
    updated_time: NotRequired["aws_sdk_glue.types.updated_timestamp.UpdatedTimestamp"]
    """<p>The date and time that a schema was updated.</p>"""


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: SchemaListItem) -> dict:
    out: dict = {}
    if "registry_name" in value:
        out["RegistryName"] = value["registry_name"]
    if "schema_name" in value:
        out["SchemaName"] = value["schema_name"]
    if "schema_arn" in value:
        out["SchemaArn"] = value["schema_arn"]
    if "description" in value:
        out["Description"] = value["description"]
    if "schema_status" in value:
        import aws_sdk_glue.types.schema_status

        out["SchemaStatus"] = aws_sdk_glue.types.schema_status.serialize_aws_json_1_1(
            value["schema_status"]
        )
    if "created_time" in value:
        out["CreatedTime"] = value["created_time"]
    if "updated_time" in value:
        out["UpdatedTime"] = value["updated_time"]
    return out


def deserialize_aws_json_1_1(data: dict) -> SchemaListItem:
    out: SchemaListItem = {}  # type: ignore[typeddict-item]
    if "RegistryName" in data:
        out["registry_name"] = data["RegistryName"]
    if "SchemaName" in data:
        out["schema_name"] = data["SchemaName"]
    if "SchemaArn" in data:
        out["schema_arn"] = data["SchemaArn"]
    if "Description" in data:
        out["description"] = data["Description"]
    if "SchemaStatus" in data:
        import aws_sdk_glue.types.schema_status

        out["schema_status"] = (
            aws_sdk_glue.types.schema_status.deserialize_aws_json_1_1(
                data["SchemaStatus"]
            )
        )
    if "CreatedTime" in data:
        out["created_time"] = data["CreatedTime"]
    if "UpdatedTime" in data:
        out["updated_time"] = data["UpdatedTime"]
    return out
