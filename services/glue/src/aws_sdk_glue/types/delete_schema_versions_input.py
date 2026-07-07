"""Generated from Smithy shape ``com.amazonaws.glue#DeleteSchemaVersionsInput``."""

from typing import TYPE_CHECKING

from typing_extensions import TypedDict

from aws_sdk_glue.errors import DeserializationError

if TYPE_CHECKING:
    import aws_sdk_glue.types.schema_id
    import aws_sdk_glue.types.versions_string


class DeleteSchemaVersionsInput(TypedDict, closed=True):
    schema_id: "aws_sdk_glue.types.schema_id.SchemaId"
    """<p>This is a wrapper structure that may contain the schema name and Amazon Resource Name (ARN).</p>"""
    versions: "aws_sdk_glue.types.versions_string.VersionsString"
    """<p>A version range may be supplied which may be of the format:</p> <ul> <li> <p>a single version number, 5</p> </li> <li> <p>a range, 5-8 : deletes versions 5, 6, 7, 8</p> </li> </ul>"""


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: DeleteSchemaVersionsInput) -> dict:
    out: dict = {}
    import aws_sdk_glue.types.schema_id

    out["SchemaId"] = aws_sdk_glue.types.schema_id.serialize_aws_json_1_1(
        value["schema_id"]
    )
    out["Versions"] = value["versions"]
    return out


def deserialize_aws_json_1_1(data: dict) -> DeleteSchemaVersionsInput:
    out: DeleteSchemaVersionsInput = {}  # type: ignore[typeddict-item]
    if "SchemaId" in data:
        import aws_sdk_glue.types.schema_id

        out["schema_id"] = aws_sdk_glue.types.schema_id.deserialize_aws_json_1_1(
            data["SchemaId"]
        )
    else:
        raise DeserializationError("DeleteSchemaVersionsInput.schema_id required")
    if "Versions" in data:
        out["versions"] = data["Versions"]
    else:
        raise DeserializationError("DeleteSchemaVersionsInput.versions required")
    return out
