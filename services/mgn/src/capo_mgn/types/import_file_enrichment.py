"""Generated from Smithy shape ``com.amazonaws.mgn#ImportFileEnrichment``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import datetime

    import capo_mgn.types.checksum
    import capo_mgn.types.enrichment_target_s3_configuration
    import capo_mgn.types.import_file_enrichment_job_id
    import capo_mgn.types.import_file_enrichment_status
    import capo_mgn.types.large_bounded_string


class ImportFileEnrichment(TypedDict, closed=True):
    job_id: NotRequired[
        "capo_mgn.types.import_file_enrichment_job_id.ImportFileEnrichmentJobID"
    ]
    """<p>The unique identifier of the import file enrichment job.</p>"""
    created_at: NotRequired["datetime.datetime"]
    """<p>The timestamp when the enrichment job was created.</p>"""
    ended_at: NotRequired["datetime.datetime"]
    """<p>The timestamp when the enrichment job completed or failed.</p>"""
    status: NotRequired[
        "capo_mgn.types.import_file_enrichment_status.ImportFileEnrichmentStatus"
    ]
    """<p>The current status of the import file enrichment job.</p>"""
    status_details: NotRequired[
        "capo_mgn.types.large_bounded_string.LargeBoundedString"
    ]
    """<p>Detailed status information about the enrichment job.</p>"""
    checksum: NotRequired["capo_mgn.types.checksum.Checksum"]
    """<p>The checksum of the enriched file for integrity verification.</p>"""
    s3_bucket_target: NotRequired[
        "capo_mgn.types.enrichment_target_s3_configuration.EnrichmentTargetS3Configuration"
    ]
    """<p>The target S3 configuration for the enriched import file.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: ImportFileEnrichment) -> dict:
    out: dict = {}
    if "job_id" in value:
        out["jobID"] = value["job_id"]
    if "created_at" in value:
        import capo_mgn.types._prelude.timestamp

        out["createdAt"] = capo_mgn.types._prelude.timestamp.serialize_json(
            value["created_at"]
        )
    if "ended_at" in value:
        import capo_mgn.types._prelude.timestamp

        out["endedAt"] = capo_mgn.types._prelude.timestamp.serialize_json(
            value["ended_at"]
        )
    if "status" in value:
        out["status"] = value["status"]
    if "status_details" in value:
        out["statusDetails"] = value["status_details"]
    if "checksum" in value:
        import capo_mgn.types.checksum

        out["checksum"] = capo_mgn.types.checksum.serialize_json(value["checksum"])
    if "s3_bucket_target" in value:
        import capo_mgn.types.enrichment_target_s3_configuration

        out["s3BucketTarget"] = (
            capo_mgn.types.enrichment_target_s3_configuration.serialize_json(
                value["s3_bucket_target"]
            )
        )
    return out


def deserialize_json(data: dict) -> ImportFileEnrichment:
    out: ImportFileEnrichment = {}  # type: ignore[typeddict-item]
    if "jobID" in data:
        out["job_id"] = data["jobID"]
    if "createdAt" in data:
        import capo_mgn.types._prelude.timestamp

        out["created_at"] = capo_mgn.types._prelude.timestamp.deserialize_json(
            data["createdAt"]
        )
    if "endedAt" in data:
        import capo_mgn.types._prelude.timestamp

        out["ended_at"] = capo_mgn.types._prelude.timestamp.deserialize_json(
            data["endedAt"]
        )
    if "status" in data:
        out["status"] = data["status"]
    if "statusDetails" in data:
        out["status_details"] = data["statusDetails"]
    if "checksum" in data:
        import capo_mgn.types.checksum

        out["checksum"] = capo_mgn.types.checksum.deserialize_json(data["checksum"])
    if "s3BucketTarget" in data:
        import capo_mgn.types.enrichment_target_s3_configuration

        out["s3_bucket_target"] = (
            capo_mgn.types.enrichment_target_s3_configuration.deserialize_json(
                data["s3BucketTarget"]
            )
        )
    return out
