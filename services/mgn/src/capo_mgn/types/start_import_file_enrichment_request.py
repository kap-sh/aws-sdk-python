"""Generated from Smithy shape ``com.amazonaws.mgn#StartImportFileEnrichmentRequest``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

from capo_mgn.errors import DeserializationError

if TYPE_CHECKING:
    import capo_mgn.types.client_idempotency_token
    import capo_mgn.types.enrichment_source_s3_configuration
    import capo_mgn.types.enrichment_target_s3_configuration
    import capo_mgn.types.ip_assignment_strategy


class StartImportFileEnrichmentRequest(TypedDict, closed=True):
    client_token: NotRequired[
        "capo_mgn.types.client_idempotency_token.ClientIdempotencyToken"
    ]
    """<p>A unique, case-sensitive identifier that you provide to ensure the idempotency of the request.</p>"""
    s3_bucket_source: "capo_mgn.types.enrichment_source_s3_configuration.EnrichmentSourceS3Configuration"
    """<p>The S3 configuration specifying the source location of the import file to be enriched.</p>"""
    s3_bucket_target: "capo_mgn.types.enrichment_target_s3_configuration.EnrichmentTargetS3Configuration"
    """<p>The S3 configuration specifying the target location where the enriched import file will be stored.</p>"""
    ip_assignment_strategy: NotRequired[
        "capo_mgn.types.ip_assignment_strategy.IpAssignmentStrategy"
    ]
    """<p>The IP assignment strategy to use when enriching the import file. Can be STATIC or DYNAMIC.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: StartImportFileEnrichmentRequest) -> dict:
    out: dict = {}
    if "client_token" in value:
        out["clientToken"] = value["client_token"]
    import capo_mgn.types.enrichment_source_s3_configuration

    out["s3BucketSource"] = (
        capo_mgn.types.enrichment_source_s3_configuration.serialize_json(
            value["s3_bucket_source"]
        )
    )
    import capo_mgn.types.enrichment_target_s3_configuration

    out["s3BucketTarget"] = (
        capo_mgn.types.enrichment_target_s3_configuration.serialize_json(
            value["s3_bucket_target"]
        )
    )
    if "ip_assignment_strategy" in value:
        out["ipAssignmentStrategy"] = value["ip_assignment_strategy"]
    return out


def deserialize_json(data: dict) -> StartImportFileEnrichmentRequest:
    out: StartImportFileEnrichmentRequest = {}  # type: ignore[typeddict-item]
    if "clientToken" in data:
        out["client_token"] = data["clientToken"]
    if "s3BucketSource" in data:
        import capo_mgn.types.enrichment_source_s3_configuration

        out["s3_bucket_source"] = (
            capo_mgn.types.enrichment_source_s3_configuration.deserialize_json(
                data["s3BucketSource"]
            )
        )
    else:
        raise DeserializationError(
            "StartImportFileEnrichmentRequest.s3_bucket_source required"
        )
    if "s3BucketTarget" in data:
        import capo_mgn.types.enrichment_target_s3_configuration

        out["s3_bucket_target"] = (
            capo_mgn.types.enrichment_target_s3_configuration.deserialize_json(
                data["s3BucketTarget"]
            )
        )
    else:
        raise DeserializationError(
            "StartImportFileEnrichmentRequest.s3_bucket_target required"
        )
    if "ipAssignmentStrategy" in data:
        out["ip_assignment_strategy"] = data["ipAssignmentStrategy"]
    return out
