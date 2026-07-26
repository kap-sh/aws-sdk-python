"""Generated from Smithy shape ``com.amazonaws.databasemigrationservice#ExportMetadataModelAssessmentResultEntry``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import capo_database_migration_service.types.string


class ExportMetadataModelAssessmentResultEntry(TypedDict, closed=True):
    s3_object_key: NotRequired["capo_database_migration_service.types.string.String"]
    """<p>The object key for the object containing the exported metadata model assessment.</p>"""
    object_url: NotRequired["capo_database_migration_service.types.string.String"]
    """<p>The URL for the object containing the exported metadata model assessment.</p>"""


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: ExportMetadataModelAssessmentResultEntry) -> dict:
    out: dict = {}
    if "s3_object_key" in value:
        out["S3ObjectKey"] = value["s3_object_key"]
    if "object_url" in value:
        out["ObjectURL"] = value["object_url"]
    return out


def deserialize_aws_json_1_1(data: dict) -> ExportMetadataModelAssessmentResultEntry:
    out: ExportMetadataModelAssessmentResultEntry = {}  # type: ignore[typeddict-item]
    if "S3ObjectKey" in data:
        out["s3_object_key"] = data["S3ObjectKey"]
    if "ObjectURL" in data:
        out["object_url"] = data["ObjectURL"]
    return out
