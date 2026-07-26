"""Generated from Smithy shape ``com.amazonaws.inspector2#GetCodeSecurityScanResponse``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import datetime

    import capo_inspector2.types.code_scan_status
    import capo_inspector2.types.code_security_resource
    import capo_inspector2.types.code_security_uuid


class GetCodeSecurityScanResponse(TypedDict, closed=True):
    scan_id: NotRequired["capo_inspector2.types.code_security_uuid.CodeSecurityUuid"]
    """<p>The unique identifier of the scan.</p>"""
    resource: NotRequired[
        "capo_inspector2.types.code_security_resource.CodeSecurityResource"
    ]
    """<p>The resource identifier for the code repository that was scanned.</p>"""
    account_id: NotRequired["str"]
    """<p>The Amazon Web Services account ID associated with the scan.</p>"""
    status: NotRequired["capo_inspector2.types.code_scan_status.CodeScanStatus"]
    """<p>The current status of the scan.</p>"""
    status_reason: NotRequired["str"]
    """<p>The reason for the current status of the scan.</p>"""
    created_at: NotRequired["datetime.datetime"]
    """<p>The timestamp when the scan was created.</p>"""
    updated_at: NotRequired["datetime.datetime"]
    """<p>The timestamp when the scan was last updated.</p>"""
    last_commit_id: NotRequired["str"]
    """<p>The identifier of the last commit that was scanned. This is only returned if the scan was successful or skipped.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: GetCodeSecurityScanResponse) -> dict:
    out: dict = {}
    if "scan_id" in value:
        out["scanId"] = value["scan_id"]
    if "resource" in value:
        import capo_inspector2.types.code_security_resource

        out["resource"] = capo_inspector2.types.code_security_resource.serialize_json(
            value["resource"]
        )
    if "account_id" in value:
        out["accountId"] = value["account_id"]
    if "status" in value:
        import capo_inspector2.types.code_scan_status

        out["status"] = capo_inspector2.types.code_scan_status.serialize_json(
            value["status"]
        )
    if "status_reason" in value:
        out["statusReason"] = value["status_reason"]
    if "created_at" in value:
        import capo_inspector2.types._prelude.timestamp

        out["createdAt"] = capo_inspector2.types._prelude.timestamp.serialize_json(
            value["created_at"]
        )
    if "updated_at" in value:
        import capo_inspector2.types._prelude.timestamp

        out["updatedAt"] = capo_inspector2.types._prelude.timestamp.serialize_json(
            value["updated_at"]
        )
    if "last_commit_id" in value:
        out["lastCommitId"] = value["last_commit_id"]
    return out


def deserialize_json(data: dict) -> GetCodeSecurityScanResponse:
    out: GetCodeSecurityScanResponse = {}  # type: ignore[typeddict-item]
    if "scanId" in data:
        out["scan_id"] = data["scanId"]
    if "resource" in data:
        import capo_inspector2.types.code_security_resource

        out["resource"] = capo_inspector2.types.code_security_resource.deserialize_json(
            data["resource"]
        )
    if "accountId" in data:
        out["account_id"] = data["accountId"]
    if "status" in data:
        import capo_inspector2.types.code_scan_status

        out["status"] = capo_inspector2.types.code_scan_status.deserialize_json(
            data["status"]
        )
    if "statusReason" in data:
        out["status_reason"] = data["statusReason"]
    if "createdAt" in data:
        import capo_inspector2.types._prelude.timestamp

        out["created_at"] = capo_inspector2.types._prelude.timestamp.deserialize_json(
            data["createdAt"]
        )
    if "updatedAt" in data:
        import capo_inspector2.types._prelude.timestamp

        out["updated_at"] = capo_inspector2.types._prelude.timestamp.deserialize_json(
            data["updatedAt"]
        )
    if "lastCommitId" in data:
        out["last_commit_id"] = data["lastCommitId"]
    return out
