"""Generated from Smithy shape ``com.amazonaws.glue#GetSchemaByDefinitionResponse``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import capo_glue.types.created_timestamp
    import capo_glue.types.data_format
    import capo_glue.types.glue_resource_arn
    import capo_glue.types.schema_version_id_string
    import capo_glue.types.schema_version_status


class GetSchemaByDefinitionResponse(TypedDict, closed=True):
    schema_version_id: NotRequired[
        "capo_glue.types.schema_version_id_string.SchemaVersionIdString"
    ]
    """<p>The schema ID of the schema version.</p>"""
    schema_arn: NotRequired["capo_glue.types.glue_resource_arn.GlueResourceArn"]
    """<p>The Amazon Resource Name (ARN) of the schema.</p>"""
    data_format: NotRequired["capo_glue.types.data_format.DataFormat"]
    """<p>The data format of the schema definition. Currently <code>AVRO</code>, <code>JSON</code> and <code>PROTOBUF</code> are supported.</p>"""
    status: NotRequired["capo_glue.types.schema_version_status.SchemaVersionStatus"]
    """<p>The status of the schema version.</p>"""
    created_time: NotRequired["capo_glue.types.created_timestamp.CreatedTimestamp"]
    """<p>The date and time the schema was created.</p>"""


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: GetSchemaByDefinitionResponse) -> dict:
    out: dict = {}
    if "schema_version_id" in value:
        out["SchemaVersionId"] = value["schema_version_id"]
    if "schema_arn" in value:
        out["SchemaArn"] = value["schema_arn"]
    if "data_format" in value:
        import capo_glue.types.data_format

        out["DataFormat"] = capo_glue.types.data_format.serialize_aws_json_1_1(
            value["data_format"]
        )
    if "status" in value:
        import capo_glue.types.schema_version_status

        out["Status"] = capo_glue.types.schema_version_status.serialize_aws_json_1_1(
            value["status"]
        )
    if "created_time" in value:
        out["CreatedTime"] = value["created_time"]
    return out


def deserialize_aws_json_1_1(data: dict) -> GetSchemaByDefinitionResponse:
    out: GetSchemaByDefinitionResponse = {}  # type: ignore[typeddict-item]
    if "SchemaVersionId" in data:
        out["schema_version_id"] = data["SchemaVersionId"]
    if "SchemaArn" in data:
        out["schema_arn"] = data["SchemaArn"]
    if "DataFormat" in data:
        import capo_glue.types.data_format

        out["data_format"] = capo_glue.types.data_format.deserialize_aws_json_1_1(
            data["DataFormat"]
        )
    if "Status" in data:
        import capo_glue.types.schema_version_status

        out["status"] = capo_glue.types.schema_version_status.deserialize_aws_json_1_1(
            data["Status"]
        )
    if "CreatedTime" in data:
        out["created_time"] = data["CreatedTime"]
    return out
