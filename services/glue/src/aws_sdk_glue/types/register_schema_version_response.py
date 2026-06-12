"""Generated from Smithy shape ``com.amazonaws.glue#RegisterSchemaVersionResponse``."""

from typing import TYPE_CHECKING, TypedDict

from typing_extensions import NotRequired

if TYPE_CHECKING:
    import aws_sdk_glue.types.schema_version_id_string
    import aws_sdk_glue.types.schema_version_status
    import aws_sdk_glue.types.version_long_number


class RegisterSchemaVersionResponse(TypedDict):
    schema_version_id: NotRequired[
        "aws_sdk_glue.types.schema_version_id_string.SchemaVersionIdString"
    ]
    """<p>The unique ID that represents the version of this schema.</p>"""
    version_number: NotRequired[
        "aws_sdk_glue.types.version_long_number.VersionLongNumber"
    ]
    """<p>The version of this schema (for sync flow only, in case this is the first version).</p>"""
    status: NotRequired["aws_sdk_glue.types.schema_version_status.SchemaVersionStatus"]
    """<p>The status of the schema version.</p>"""


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: RegisterSchemaVersionResponse) -> dict:
    out: dict = {}
    if "schema_version_id" in value:
        out["SchemaVersionId"] = value["schema_version_id"]
    if "version_number" in value:
        out["VersionNumber"] = value["version_number"]
    if "status" in value:
        import aws_sdk_glue.types.schema_version_status

        out["Status"] = aws_sdk_glue.types.schema_version_status.serialize_aws_json_1_1(
            value["status"]
        )
    return out


def deserialize_aws_json_1_1(data: dict) -> RegisterSchemaVersionResponse:
    out: RegisterSchemaVersionResponse = {}  # type: ignore[typeddict-item]
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
    return out
