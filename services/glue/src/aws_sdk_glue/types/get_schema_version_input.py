"""Generated from Smithy shape ``com.amazonaws.glue#GetSchemaVersionInput``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import aws_sdk_glue.types.schema_id
    import aws_sdk_glue.types.schema_version_id_string
    import aws_sdk_glue.types.schema_version_number


class GetSchemaVersionInput(TypedDict, closed=True):
    schema_id: NotRequired["aws_sdk_glue.types.schema_id.SchemaId"]
    """<p>This is a wrapper structure to contain schema identity fields. The structure contains:</p> <ul> <li> <p>SchemaId$SchemaArn: The Amazon Resource Name (ARN) of the schema. Either <code>SchemaArn</code> or <code>SchemaName</code> and <code>RegistryName</code> has to be provided.</p> </li> <li> <p>SchemaId$SchemaName: The name of the schema. Either <code>SchemaArn</code> or <code>SchemaName</code> and <code>RegistryName</code> has to be provided.</p> </li> </ul>"""
    schema_version_id: NotRequired[
        "aws_sdk_glue.types.schema_version_id_string.SchemaVersionIdString"
    ]
    """<p>The <code>SchemaVersionId</code> of the schema version. This field is required for fetching by schema ID. Either this or the <code>SchemaId</code> wrapper has to be provided.</p>"""
    schema_version_number: NotRequired[
        "aws_sdk_glue.types.schema_version_number.SchemaVersionNumber"
    ]
    """<p>The version number of the schema.</p>"""


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: GetSchemaVersionInput) -> dict:
    out: dict = {}
    if "schema_id" in value:
        import aws_sdk_glue.types.schema_id

        out["SchemaId"] = aws_sdk_glue.types.schema_id.serialize_aws_json_1_1(
            value["schema_id"]
        )
    if "schema_version_id" in value:
        out["SchemaVersionId"] = value["schema_version_id"]
    if "schema_version_number" in value:
        import aws_sdk_glue.types.schema_version_number

        out["SchemaVersionNumber"] = (
            aws_sdk_glue.types.schema_version_number.serialize_aws_json_1_1(
                value["schema_version_number"]
            )
        )
    return out


def deserialize_aws_json_1_1(data: dict) -> GetSchemaVersionInput:
    out: GetSchemaVersionInput = {}  # type: ignore[typeddict-item]
    if "SchemaId" in data:
        import aws_sdk_glue.types.schema_id

        out["schema_id"] = aws_sdk_glue.types.schema_id.deserialize_aws_json_1_1(
            data["SchemaId"]
        )
    if "SchemaVersionId" in data:
        out["schema_version_id"] = data["SchemaVersionId"]
    if "SchemaVersionNumber" in data:
        import aws_sdk_glue.types.schema_version_number

        out["schema_version_number"] = (
            aws_sdk_glue.types.schema_version_number.deserialize_aws_json_1_1(
                data["SchemaVersionNumber"]
            )
        )
    return out
