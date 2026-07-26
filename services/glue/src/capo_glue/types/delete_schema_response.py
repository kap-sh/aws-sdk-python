"""Generated from Smithy shape ``com.amazonaws.glue#DeleteSchemaResponse``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import capo_glue.types.glue_resource_arn
    import capo_glue.types.schema_registry_name_string
    import capo_glue.types.schema_status


class DeleteSchemaResponse(TypedDict, closed=True):
    schema_arn: NotRequired["capo_glue.types.glue_resource_arn.GlueResourceArn"]
    """<p>The Amazon Resource Name (ARN) of the schema being deleted.</p>"""
    schema_name: NotRequired[
        "capo_glue.types.schema_registry_name_string.SchemaRegistryNameString"
    ]
    """<p>The name of the schema being deleted.</p>"""
    status: NotRequired["capo_glue.types.schema_status.SchemaStatus"]
    """<p>The status of the schema.</p>"""


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: DeleteSchemaResponse) -> dict:
    out: dict = {}
    if "schema_arn" in value:
        out["SchemaArn"] = value["schema_arn"]
    if "schema_name" in value:
        out["SchemaName"] = value["schema_name"]
    if "status" in value:
        import capo_glue.types.schema_status

        out["Status"] = capo_glue.types.schema_status.serialize_aws_json_1_1(
            value["status"]
        )
    return out


def deserialize_aws_json_1_1(data: dict) -> DeleteSchemaResponse:
    out: DeleteSchemaResponse = {}  # type: ignore[typeddict-item]
    if "SchemaArn" in data:
        out["schema_arn"] = data["SchemaArn"]
    if "SchemaName" in data:
        out["schema_name"] = data["SchemaName"]
    if "Status" in data:
        import capo_glue.types.schema_status

        out["status"] = capo_glue.types.schema_status.deserialize_aws_json_1_1(
            data["Status"]
        )
    return out
