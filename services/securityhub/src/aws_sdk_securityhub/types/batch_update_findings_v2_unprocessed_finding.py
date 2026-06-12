"""Generated from Smithy shape ``com.amazonaws.securityhub#BatchUpdateFindingsV2UnprocessedFinding``."""

from typing import TYPE_CHECKING, TypedDict

from typing_extensions import NotRequired

if TYPE_CHECKING:
    import aws_sdk_securityhub.types.batch_update_findings_v2_unprocessed_finding_error_code
    import aws_sdk_securityhub.types.non_empty_string
    import aws_sdk_securityhub.types.ocsf_finding_identifier


class BatchUpdateFindingsV2UnprocessedFinding(TypedDict):
    finding_identifier: NotRequired[
        "aws_sdk_securityhub.types.ocsf_finding_identifier.OcsfFindingIdentifier"
    ]
    """<p>The finding identifier of an unprocessed finding.</p>"""
    metadata_uid: NotRequired[
        "aws_sdk_securityhub.types.non_empty_string.NonEmptyString"
    ]
    """<p>The metadata.uid of an unprocessed finding.</p>"""
    error_code: NotRequired[
        "aws_sdk_securityhub.types.batch_update_findings_v2_unprocessed_finding_error_code.BatchUpdateFindingsV2UnprocessedFindingErrorCode"
    ]
    """<p>Indicates the specific type of error preventing successful processing of a finding during a batch update operation.</p>"""
    error_message: NotRequired[
        "aws_sdk_securityhub.types.non_empty_string.NonEmptyString"
    ]
    """<p>A detailed description of why a finding could not be processed during a batch update operation.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: BatchUpdateFindingsV2UnprocessedFinding) -> dict:
    out: dict = {}
    if "finding_identifier" in value:
        import aws_sdk_securityhub.types.ocsf_finding_identifier

        out["FindingIdentifier"] = (
            aws_sdk_securityhub.types.ocsf_finding_identifier.serialize_json(
                value["finding_identifier"]
            )
        )
    if "metadata_uid" in value:
        out["MetadataUid"] = value["metadata_uid"]
    if "error_code" in value:
        import aws_sdk_securityhub.types.batch_update_findings_v2_unprocessed_finding_error_code

        out["ErrorCode"] = (
            aws_sdk_securityhub.types.batch_update_findings_v2_unprocessed_finding_error_code.serialize_json(
                value["error_code"]
            )
        )
    if "error_message" in value:
        out["ErrorMessage"] = value["error_message"]
    return out


def deserialize_json(data: dict) -> BatchUpdateFindingsV2UnprocessedFinding:
    out: BatchUpdateFindingsV2UnprocessedFinding = {}  # type: ignore[typeddict-item]
    if "FindingIdentifier" in data:
        import aws_sdk_securityhub.types.ocsf_finding_identifier

        out["finding_identifier"] = (
            aws_sdk_securityhub.types.ocsf_finding_identifier.deserialize_json(
                data["FindingIdentifier"]
            )
        )
    if "MetadataUid" in data:
        out["metadata_uid"] = data["MetadataUid"]
    if "ErrorCode" in data:
        import aws_sdk_securityhub.types.batch_update_findings_v2_unprocessed_finding_error_code

        out["error_code"] = (
            aws_sdk_securityhub.types.batch_update_findings_v2_unprocessed_finding_error_code.deserialize_json(
                data["ErrorCode"]
            )
        )
    if "ErrorMessage" in data:
        out["error_message"] = data["ErrorMessage"]
    return out
