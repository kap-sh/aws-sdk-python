"""Generated from Smithy shape ``com.amazonaws.glue#SchemaVersionListItem``."""

from typing import TYPE_CHECKING, TypedDict

from typing_extensions import NotRequired

if TYPE_CHECKING:
    import aws_sdk_glue.types.created_timestamp
    import aws_sdk_glue.types.glue_resource_arn
    import aws_sdk_glue.types.schema_version_id_string
    import aws_sdk_glue.types.schema_version_status
    import aws_sdk_glue.types.version_long_number


class SchemaVersionListItem(TypedDict):
    schema_arn: NotRequired["aws_sdk_glue.types.glue_resource_arn.GlueResourceArn"]
    """<p>The Amazon Resource Name (ARN) of the schema.</p>"""
    schema_version_id: NotRequired[
        "aws_sdk_glue.types.schema_version_id_string.SchemaVersionIdString"
    ]
    """<p>The unique identifier of the schema version.</p>"""
    version_number: NotRequired[
        "aws_sdk_glue.types.version_long_number.VersionLongNumber"
    ]
    """<p>The version number of the schema.</p>"""
    status: NotRequired["aws_sdk_glue.types.schema_version_status.SchemaVersionStatus"]
    """<p>The status of the schema version.</p>"""
    created_time: NotRequired["aws_sdk_glue.types.created_timestamp.CreatedTimestamp"]
    """<p>The date and time the schema version was created.</p>"""


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: SchemaVersionListItem) -> dict:
    out: dict = {}
    if "schema_arn" in value:
        out["SchemaArn"] = value["schema_arn"]
    if "schema_version_id" in value:
        out["SchemaVersionId"] = value["schema_version_id"]
    if "version_number" in value:
        out["VersionNumber"] = value["version_number"]
    if "status" in value:
        import aws_sdk_glue.types.schema_version_status

        out["Status"] = aws_sdk_glue.types.schema_version_status.serialize_aws_json_1_1(
            value["status"]
        )
    if "created_time" in value:
        out["CreatedTime"] = value["created_time"]
    return out


def deserialize_aws_json_1_1(data: dict) -> SchemaVersionListItem:
    out: SchemaVersionListItem = {}  # type: ignore[typeddict-item]
    if "SchemaArn" in data:
        out["schema_arn"] = data["SchemaArn"]
    if "SchemaVersionId" in data:
        out["schema_version_id"] = data["SchemaVersionId"]
    if "VersionNumber" in data:
        out["version_number"] = data["VersionNumber"]
    if "Status" in data:
        import aws_sdk_glue.types.schema_version_status

        out["status"] = (
            aws_sdk_glue.types.schema_version_status.deserialize_aws_json_1_1(
                data["Status"]
            )
        )
    if "CreatedTime" in data:
        out["created_time"] = data["CreatedTime"]
    return out
