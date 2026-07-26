"""Generated from Smithy shape ``com.amazonaws.mpa#GetApprovalTeamResponseApprover``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import capo_mpa.types.approver_last_activity
    import capo_mpa.types.identity_id
    import capo_mpa.types.identity_status
    import capo_mpa.types.iso_timestamp
    import capo_mpa.types.mfa_methods
    import capo_mpa.types.participant_id
    import capo_mpa.types.session_arn
    import capo_mpa.types.string


class GetApprovalTeamResponseApprover(TypedDict, closed=True):
    approver_id: NotRequired["capo_mpa.types.participant_id.ParticipantId"]
    """<p>ID for the approver.</p>"""
    response_time: NotRequired["capo_mpa.types.iso_timestamp.IsoTimestamp"]
    """<p>Timestamp when the approver responded to an approval team invitation.</p>"""
    primary_identity_id: NotRequired["capo_mpa.types.identity_id.IdentityId"]
    """<p>ID for the user.</p>"""
    primary_identity_source_arn: NotRequired["capo_mpa.types.string.String"]
    """<p>Amazon Resource Name (ARN) for the identity source. The identity source manages the user authentication for approvers.</p>"""
    primary_identity_status: NotRequired[
        "capo_mpa.types.identity_status.IdentityStatus"
    ]
    """<p>Status for the identity source. For example, if an approver has accepted a team invitation with a user authentication method managed by the identity source.</p>"""
    last_activity: NotRequired[
        "capo_mpa.types.approver_last_activity.ApproverLastActivity"
    ]
    """<p>Last Activity performed by the approver.</p>"""
    last_activity_time: NotRequired["capo_mpa.types.iso_timestamp.IsoTimestamp"]
    """<p>Timestamp when the approver last responded to an operation or invitation request.</p>"""
    pending_baseline_session_arn: NotRequired["capo_mpa.types.session_arn.SessionArn"]
    """<p>Amazon Resource Name (ARN) for the pending baseline session.</p>"""
    mfa_methods: NotRequired["capo_mpa.types.mfa_methods.MfaMethods"]
    """<p>Multi-factor authentication configuration for the approver</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: GetApprovalTeamResponseApprover) -> dict:
    out: dict = {}
    if "approver_id" in value:
        out["ApproverId"] = value["approver_id"]
    if "response_time" in value:
        import capo_mpa.types.iso_timestamp

        out["ResponseTime"] = capo_mpa.types.iso_timestamp.serialize_json(
            value["response_time"]
        )
    if "primary_identity_id" in value:
        out["PrimaryIdentityId"] = value["primary_identity_id"]
    if "primary_identity_source_arn" in value:
        out["PrimaryIdentitySourceArn"] = value["primary_identity_source_arn"]
    if "primary_identity_status" in value:
        import capo_mpa.types.identity_status

        out["PrimaryIdentityStatus"] = capo_mpa.types.identity_status.serialize_json(
            value["primary_identity_status"]
        )
    if "last_activity" in value:
        import capo_mpa.types.approver_last_activity

        out["LastActivity"] = capo_mpa.types.approver_last_activity.serialize_json(
            value["last_activity"]
        )
    if "last_activity_time" in value:
        import capo_mpa.types.iso_timestamp

        out["LastActivityTime"] = capo_mpa.types.iso_timestamp.serialize_json(
            value["last_activity_time"]
        )
    if "pending_baseline_session_arn" in value:
        out["PendingBaselineSessionArn"] = value["pending_baseline_session_arn"]
    if "mfa_methods" in value:
        import capo_mpa.types.mfa_methods

        out["MfaMethods"] = capo_mpa.types.mfa_methods.serialize_json(
            value["mfa_methods"]
        )
    return out


def deserialize_json(data: dict) -> GetApprovalTeamResponseApprover:
    out: GetApprovalTeamResponseApprover = {}  # type: ignore[typeddict-item]
    if "ApproverId" in data:
        out["approver_id"] = data["ApproverId"]
    if "ResponseTime" in data:
        import capo_mpa.types.iso_timestamp

        out["response_time"] = capo_mpa.types.iso_timestamp.deserialize_json(
            data["ResponseTime"]
        )
    if "PrimaryIdentityId" in data:
        out["primary_identity_id"] = data["PrimaryIdentityId"]
    if "PrimaryIdentitySourceArn" in data:
        out["primary_identity_source_arn"] = data["PrimaryIdentitySourceArn"]
    if "PrimaryIdentityStatus" in data:
        import capo_mpa.types.identity_status

        out["primary_identity_status"] = (
            capo_mpa.types.identity_status.deserialize_json(
                data["PrimaryIdentityStatus"]
            )
        )
    if "LastActivity" in data:
        import capo_mpa.types.approver_last_activity

        out["last_activity"] = capo_mpa.types.approver_last_activity.deserialize_json(
            data["LastActivity"]
        )
    if "LastActivityTime" in data:
        import capo_mpa.types.iso_timestamp

        out["last_activity_time"] = capo_mpa.types.iso_timestamp.deserialize_json(
            data["LastActivityTime"]
        )
    if "PendingBaselineSessionArn" in data:
        out["pending_baseline_session_arn"] = data["PendingBaselineSessionArn"]
    if "MfaMethods" in data:
        import capo_mpa.types.mfa_methods

        out["mfa_methods"] = capo_mpa.types.mfa_methods.deserialize_json(
            data["MfaMethods"]
        )
    return out
