"""Generated from Smithy shape ``com.amazonaws.glue#GetSchemaInput``."""

from typing import TYPE_CHECKING

from typing_extensions import TypedDict

from aws_sdk_glue.errors import DeserializationError

if TYPE_CHECKING:
    import aws_sdk_glue.types.schema_id


class GetSchemaInput(TypedDict, closed=True):
    schema_id: "aws_sdk_glue.types.schema_id.SchemaId"
    """<p>This is a wrapper structure to contain schema identity fields. The structure contains:</p> <ul> <li> <p>SchemaId$SchemaArn: The Amazon Resource Name (ARN) of the schema. Either <code>SchemaArn</code> or <code>SchemaName</code> and <code>RegistryName</code> has to be provided.</p> </li> <li> <p>SchemaId$SchemaName: The name of the schema. Either <code>SchemaArn</code> or <code>SchemaName</code> and <code>RegistryName</code> has to be provided.</p> </li> </ul>"""


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: GetSchemaInput) -> dict:
    out: dict = {}
    import aws_sdk_glue.types.schema_id

    out["SchemaId"] = aws_sdk_glue.types.schema_id.serialize_aws_json_1_1(
        value["schema_id"]
    )
    return out


def deserialize_aws_json_1_1(data: dict) -> GetSchemaInput:
    out: GetSchemaInput = {}  # type: ignore[typeddict-item]
    if "SchemaId" in data:
        import aws_sdk_glue.types.schema_id

        out["schema_id"] = aws_sdk_glue.types.schema_id.deserialize_aws_json_1_1(
            data["SchemaId"]
        )
    else:
        raise DeserializationError("GetSchemaInput.schema_id required")
    return out
