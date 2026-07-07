"""Generated from Smithy shape ``com.amazonaws.backup#LatestMpaApprovalTeamUpdate``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import aws_sdk_backup.types.arn
    import aws_sdk_backup.types.mpa_session_status
    import aws_sdk_backup.types.string
    import aws_sdk_backup.types.timestamp


class LatestMpaApprovalTeamUpdate(TypedDict, closed=True):
    mpa_session_arn: NotRequired["aws_sdk_backup.types.arn.ARN"]
    """<p>The ARN of the MPA session associated with this update.</p>"""
    status: NotRequired["aws_sdk_backup.types.mpa_session_status.MpaSessionStatus"]
    """<p>The current status of the MPA approval team update.</p>"""
    status_message: NotRequired["aws_sdk_backup.types.string.string"]
    """<p>A message describing the current status of the MPA approval team update.</p>"""
    initiation_date: NotRequired["aws_sdk_backup.types.timestamp.timestamp"]
    """<p>The date and time when the MPA approval team update was initiated.</p>"""
    expiry_date: NotRequired["aws_sdk_backup.types.timestamp.timestamp"]
    """<p>The date and time when the MPA approval team update will expire.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: LatestMpaApprovalTeamUpdate) -> dict:
    out: dict = {}
    if "mpa_session_arn" in value:
        out["MpaSessionArn"] = value["mpa_session_arn"]
    if "status" in value:
        import aws_sdk_backup.types.mpa_session_status

        out["Status"] = aws_sdk_backup.types.mpa_session_status.serialize_json(
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


def deserialize_json(data: dict) -> LatestMpaApprovalTeamUpdate:
    out: LatestMpaApprovalTeamUpdate = {}  # type: ignore[typeddict-item]
    if "MpaSessionArn" in data:
        out["mpa_session_arn"] = data["MpaSessionArn"]
    if "Status" in data:
        import aws_sdk_backup.types.mpa_session_status

        out["status"] = aws_sdk_backup.types.mpa_session_status.deserialize_json(
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
