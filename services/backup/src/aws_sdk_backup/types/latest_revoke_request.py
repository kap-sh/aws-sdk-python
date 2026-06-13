"""Generated from Smithy shape ``com.amazonaws.backup#LatestRevokeRequest``."""

from typing import TYPE_CHECKING, TypedDict

from typing_extensions import NotRequired

if TYPE_CHECKING:
    import aws_sdk_backup.types.mpa_revoke_session_status
    import aws_sdk_backup.types.string
    import aws_sdk_backup.types.timestamp


class LatestRevokeRequest(TypedDict):
    mpa_session_arn: NotRequired["aws_sdk_backup.types.string.string"]
    """<p>The ARN of the MPA session associated with this revoke request.</p>"""
    status: NotRequired[
        "aws_sdk_backup.types.mpa_revoke_session_status.MpaRevokeSessionStatus"
    ]
    """<p>The current status of the revoke request.</p>"""
    status_message: NotRequired["aws_sdk_backup.types.string.string"]
    """<p>A message describing the current status of the revoke request.</p>"""
    initiation_date: NotRequired["aws_sdk_backup.types.timestamp.timestamp"]
    """<p>The date and time when the revoke request was initiated.</p>"""
    expiry_date: NotRequired["aws_sdk_backup.types.timestamp.timestamp"]
    """<p>The date and time when the revoke request will expire.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: LatestRevokeRequest) -> dict:
    out: dict = {}
    if "mpa_session_arn" in value:
        out["MpaSessionArn"] = value["mpa_session_arn"]
    if "status" in value:
        import aws_sdk_backup.types.mpa_revoke_session_status

        out["Status"] = aws_sdk_backup.types.mpa_revoke_session_status.serialize_json(
            value["status"]
        )
    if "status_message" in value:
        out["StatusMessage"] = value["status_message"]
    if "initiation_date" in value:
        import aws_sdk_backup.types.timestamp

        out["InitiationDate"] = aws_sdk_backup.types.timestamp.serialize_json(
            value["initiation_date"]
        )
    if "expiry_date" in value:
        import aws_sdk_backup.types.timestamp

        out["ExpiryDate"] = aws_sdk_backup.types.timestamp.serialize_json(
            value["expiry_date"]
        )
    return out


def deserialize_json(data: dict) -> LatestRevokeRequest:
    out: LatestRevokeRequest = {}  # type: ignore[typeddict-item]
    if "MpaSessionArn" in data:
        out["mpa_session_arn"] = data["MpaSessionArn"]
    if "Status" in data:
        import aws_sdk_backup.types.mpa_revoke_session_status

        out["status"] = aws_sdk_backup.types.mpa_revoke_session_status.deserialize_json(
            data["Status"]
        )
    if "StatusMessage" in data:
        out["status_message"] = data["StatusMessage"]
    if "InitiationDate" in data:
        import aws_sdk_backup.types.timestamp

        out["initiation_date"] = aws_sdk_backup.types.timestamp.deserialize_json(
            data["InitiationDate"]
        )
    if "ExpiryDate" in data:
        import aws_sdk_backup.types.timestamp

        out["expiry_date"] = aws_sdk_backup.types.timestamp.deserialize_json(
            data["ExpiryDate"]
        )
    return out
