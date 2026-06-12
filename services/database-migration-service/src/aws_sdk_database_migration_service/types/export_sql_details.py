"""Generated from Smithy shape ``com.amazonaws.databasemigrationservice#ExportSqlDetails``."""

from typing import TYPE_CHECKING, TypedDict

from typing_extensions import NotRequired

if TYPE_CHECKING:
    import aws_sdk_database_migration_service.types.string


class ExportSqlDetails(TypedDict):
    s3_object_key: NotRequired["aws_sdk_database_migration_service.types.string.String"]
    """<p>The Amazon S3 object key for the object containing the exported metadata model assessment.</p>"""
    object_url: NotRequired["aws_sdk_database_migration_service.types.string.String"]
    """<p>The URL for the object containing the exported metadata model assessment.</p>"""


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: ExportSqlDetails) -> dict:
    out: dict = {}
    if "s3_object_key" in value:
        out["S3ObjectKey"] = value["s3_object_key"]
    if "object_url" in value:
        out["ObjectURL"] = value["object_url"]
    return out


def deserialize_aws_json_1_1(data: dict) -> ExportSqlDetails:
    out: ExportSqlDetails = {}  # type: ignore[typeddict-item]
    if "S3ObjectKey" in data:
        out["s3_object_key"] = data["S3ObjectKey"]
    if "ObjectURL" in data:
        out["object_url"] = data["ObjectURL"]
    return out
