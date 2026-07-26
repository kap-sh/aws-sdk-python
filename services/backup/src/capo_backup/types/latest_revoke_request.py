"""Generated from Smithy shape ``com.amazonaws.backup#LatestRevokeRequest``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import capo_backup.types.mpa_revoke_session_status
    import capo_backup.types.string
    import capo_backup.types.timestamp


class LatestRevokeRequest(TypedDict, closed=True):
    mpa_session_arn: NotRequired["capo_backup.types.string.string"]
    """<p>The ARN of the MPA session associated with this revoke request.</p>"""
    status: NotRequired[
        "capo_backup.types.mpa_revoke_session_status.MpaRevokeSessionStatus"
    ]
    """<p>The current status of the revoke request.</p>"""
    status_message: NotRequired["capo_backup.types.string.string"]
    """<p>A message describing the current status of the revoke request.</p>"""
    initiation_date: NotRequired["capo_backup.types.timestamp.timestamp"]
    """<p>The date and time when the revoke request was initiated.</p>"""
    expiry_date: NotRequired["capo_backup.types.timestamp.timestamp"]
    """<p>The date and time when the revoke request will expire.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: LatestRevokeRequest) -> dict:
    out: dict = {}
    if "mpa_session_arn" in value:
        out["MpaSessionArn"] = value["mpa_session_arn"]
    if "status" in value:
        import capo_backup.types.mpa_revoke_session_status

        out["Status"] = capo_backup.types.mpa_revoke_session_status.serialize_json(
            value["status"]
        )
    if "status_message" in value:
        out["StatusMessage"] = value["status_message"]
    if "initiation_date" in value:
        import capo_backup.types.timestamp

        out["InitiationDate"] = capo_backup.types.timestamp.serialize_json(
            value["initiation_date"]
        )
    if "expiry_date" in value:
        import capo_backup.types.timestamp

        out["ExpiryDate"] = capo_backup.types.timestamp.serialize_json(
            value["expiry_date"]
        )
    return out


def deserialize_json(data: dict) -> LatestRevokeRequest:
    out: LatestRevokeRequest = {}  # type: ignore[typeddict-item]
    if "MpaSessionArn" in data:
        out["mpa_session_arn"] = data["MpaSessionArn"]
    if "Status" in data:
        import capo_backup.types.mpa_revoke_session_status

        out["status"] = capo_backup.types.mpa_revoke_session_status.deserialize_json(
            data["Status"]
        )
    if "StatusMessage" in data:
        out["status_message"] = data["StatusMessage"]
    if "InitiationDate" in data:
        import capo_backup.types.timestamp

        out["initiation_date"] = capo_backup.types.timestamp.deserialize_json(
            data["InitiationDate"]
        )
    if "ExpiryDate" in data:
        import capo_backup.types.timestamp

        out["expiry_date"] = capo_backup.types.timestamp.deserialize_json(
            data["ExpiryDate"]
        )
    return out
