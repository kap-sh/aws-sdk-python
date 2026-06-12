"""Generated from Smithy shape ``com.amazonaws.glue#SchemaReference``."""

from typing import TYPE_CHECKING, TypedDict

from typing_extensions import NotRequired

if TYPE_CHECKING:
    import aws_sdk_glue.types.schema_id
    import aws_sdk_glue.types.schema_version_id_string
    import aws_sdk_glue.types.version_long_number


class SchemaReference(TypedDict):
    schema_id: NotRequired["aws_sdk_glue.types.schema_id.SchemaId"]
    """<p>A structure that contains schema identity fields. Either this or the <code>SchemaVersionId</code> has to be provided.</p>"""
    schema_version_id: NotRequired[
        "aws_sdk_glue.types.schema_version_id_string.SchemaVersionIdString"
    ]
    """<p>The unique ID assigned to a version of the schema. Either this or the <code>SchemaId</code> has to be provided.</p>"""
    schema_version_number: NotRequired[
        "aws_sdk_glue.types.version_long_number.VersionLongNumber"
    ]
    """<p>The version number of the schema.</p>"""


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: SchemaReference) -> dict:
    out: dict = {}
    if "schema_id" in value:
        import aws_sdk_glue.types.schema_id

        out["SchemaId"] = aws_sdk_glue.types.schema_id.serialize_aws_json_1_1(
            value["schema_id"]
        )
    if "schema_version_id" in value:
        out["SchemaVersionId"] = value["schema_version_id"]
    if "schema_version_number" in value:
        out["SchemaVersionNumber"] = value["schema_version_number"]
    return out


def deserialize_aws_json_1_1(data: dict) -> SchemaReference:
    out: SchemaReference = {}  # type: ignore[typeddict-item]
    if "SchemaId" in data:
        import aws_sdk_glue.types.schema_id

        out["schema_id"] = aws_sdk_glue.types.schema_id.deserialize_aws_json_1_1(
            data["SchemaId"]
        )
    if "SchemaVersionId" in data:
        out["schema_version_id"] = data["SchemaVersionId"]
    if "SchemaVersionNumber" in data:
        out["schema_version_number"] = data["SchemaVersionNumber"]
    return out
