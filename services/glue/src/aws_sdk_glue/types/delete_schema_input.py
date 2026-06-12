"""Generated from Smithy shape ``com.amazonaws.glue#DeleteSchemaInput``."""

from typing import TYPE_CHECKING, TypedDict

from aws_sdk_glue.errors import DeserializationError

if TYPE_CHECKING:
    import aws_sdk_glue.types.schema_id


class DeleteSchemaInput(TypedDict):
    schema_id: "aws_sdk_glue.types.schema_id.SchemaId"
    """<p>This is a wrapper structure that may contain the schema name and Amazon Resource Name (ARN).</p>"""


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: DeleteSchemaInput) -> dict:
    out: dict = {}
    import aws_sdk_glue.types.schema_id

    out["SchemaId"] = aws_sdk_glue.types.schema_id.serialize_aws_json_1_1(
        value["schema_id"]
    )
    return out


def deserialize_aws_json_1_1(data: dict) -> DeleteSchemaInput:
    out: DeleteSchemaInput = {}  # type: ignore[typeddict-item]
    if "SchemaId" in data:
        import aws_sdk_glue.types.schema_id

        out["schema_id"] = aws_sdk_glue.types.schema_id.deserialize_aws_json_1_1(
            data["SchemaId"]
        )
    else:
        raise DeserializationError("DeleteSchemaInput.schema_id required")
    return out
