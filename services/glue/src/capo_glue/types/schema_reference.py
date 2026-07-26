"""Generated from Smithy shape ``com.amazonaws.glue#SchemaReference``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import capo_glue.types.schema_id
    import capo_glue.types.schema_version_id_string
    import capo_glue.types.version_long_number


class SchemaReference(TypedDict, closed=True):
    schema_id: NotRequired["capo_glue.types.schema_id.SchemaId"]
    """<p>A structure that contains schema identity fields. Either this or the <code>SchemaVersionId</code> has to be provided.</p>"""
    schema_version_id: NotRequired[
        "capo_glue.types.schema_version_id_string.SchemaVersionIdString"
    ]
    """<p>The unique ID assigned to a version of the schema. Either this or the <code>SchemaId</code> has to be provided.</p>"""
    schema_version_number: NotRequired[
        "capo_glue.types.version_long_number.VersionLongNumber"
    ]
    """<p>The version number of the schema.</p>"""


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: SchemaReference) -> dict:
    out: dict = {}
    if "schema_id" in value:
        import capo_glue.types.schema_id

        out["SchemaId"] = capo_glue.types.schema_id.serialize_aws_json_1_1(
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
        import capo_glue.types.schema_id

        out["schema_id"] = capo_glue.types.schema_id.deserialize_aws_json_1_1(
            data["SchemaId"]
        )
    if "SchemaVersionId" in data:
        out["schema_version_id"] = data["SchemaVersionId"]
    if "SchemaVersionNumber" in data:
        out["schema_version_number"] = data["SchemaVersionNumber"]
    return out
