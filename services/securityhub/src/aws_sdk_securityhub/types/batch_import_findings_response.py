"""Generated from Smithy shape ``com.amazonaws.securityhub#BatchImportFindingsResponse``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import aws_sdk_securityhub.types.import_findings_error_list
    import aws_sdk_securityhub.types.integer


class BatchImportFindingsResponse(TypedDict, closed=True):
    failed_count: NotRequired["aws_sdk_securityhub.types.integer.Integer"]
    """<p>The number of findings that failed to import.</p>"""
    success_count: NotRequired["aws_sdk_securityhub.types.integer.Integer"]
    """<p>The number of findings that were successfully imported.</p>"""
    failed_findings: NotRequired[
        "aws_sdk_securityhub.types.import_findings_error_list.ImportFindingsErrorList"
    ]
    """<p>The list of findings that failed to import.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: BatchImportFindingsResponse) -> dict:
    out: dict = {}
    if "failed_count" in value:
        out["FailedCount"] = value["failed_count"]
    if "success_count" in value:
        out["SuccessCount"] = value["success_count"]
    if "failed_findings" in value:
        import aws_sdk_securityhub.types.import_findings_error_list

        out["FailedFindings"] = (
            aws_sdk_securityhub.types.import_findings_error_list.serialize_json(
                value["failed_findings"]
            )
        )
    return out


def deserialize_json(data: dict) -> BatchImportFindingsResponse:
    out: BatchImportFindingsResponse = {}  # type: ignore[typeddict-item]
    if "FailedCount" in data:
        out["failed_count"] = data["FailedCount"]
    if "SuccessCount" in data:
        out["success_count"] = data["SuccessCount"]
    if "FailedFindings" in data:
        import aws_sdk_securityhub.types.import_findings_error_list

        out["failed_findings"] = (
            aws_sdk_securityhub.types.import_findings_error_list.deserialize_json(
                data["FailedFindings"]
            )
        )
    return out
