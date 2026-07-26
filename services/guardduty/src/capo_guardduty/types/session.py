"""Generated from Smithy shape ``com.amazonaws.guardduty#Session``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import capo_guardduty.types.mfa_status
    import capo_guardduty.types.string
    import capo_guardduty.types.timestamp


class Session(TypedDict, closed=True):
    uid: NotRequired["capo_guardduty.types.string.String"]
    """<p>The unique identifier of the session.</p>"""
    mfa_status: NotRequired["capo_guardduty.types.mfa_status.MfaStatus"]
    """<p>Indicates whether or not multi-factor authencation (MFA) was used during authentication.</p> <p>In Amazon Web Services CloudTrail, you can find this value as <code>userIdentity.sessionContext.attributes.mfaAuthenticated</code>.</p>"""
    created_time: NotRequired["capo_guardduty.types.timestamp.Timestamp"]
    """<p>The timestamp for when the session was created.</p> <p>In Amazon Web Services CloudTrail, you can find this value as <code>userIdentity.sessionContext.attributes.creationDate</code>.</p>"""
    issuer: NotRequired["capo_guardduty.types.string.String"]
    """<p>Identifier of the session issuer.</p> <p>In Amazon Web Services CloudTrail, you can find this value as <code>userIdentity.sessionContext.sessionIssuer.arn</code>.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: Session) -> dict:
    out: dict = {}
    if "uid" in value:
        out["uid"] = value["uid"]
    if "mfa_status" in value:
        import capo_guardduty.types.mfa_status

        out["mfaStatus"] = capo_guardduty.types.mfa_status.serialize_json(
            value["mfa_status"]
        )
    if "created_time" in value:
        import capo_guardduty.types.timestamp

        out["createdTime"] = capo_guardduty.types.timestamp.serialize_json(
            value["created_time"]
        )
    if "issuer" in value:
        out["issuer"] = value["issuer"]
    return out


def deserialize_json(data: dict) -> Session:
    out: Session = {}  # type: ignore[typeddict-item]
    if "uid" in data:
        out["uid"] = data["uid"]
    if "mfaStatus" in data:
        import capo_guardduty.types.mfa_status

        out["mfa_status"] = capo_guardduty.types.mfa_status.deserialize_json(
            data["mfaStatus"]
        )
    if "createdTime" in data:
        import capo_guardduty.types.timestamp

        out["created_time"] = capo_guardduty.types.timestamp.deserialize_json(
            data["createdTime"]
        )
    if "issuer" in data:
        out["issuer"] = data["issuer"]
    return out
