"""Generated from Smithy shape ``com.amazonaws.pinpointemail#IdentityInfo``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import capo_pinpoint_email.types.enabled
    import capo_pinpoint_email.types.identity
    import capo_pinpoint_email.types.identity_type


class IdentityInfo(TypedDict, closed=True):
    identity_type: NotRequired["capo_pinpoint_email.types.identity_type.IdentityType"]
    """<p>The email identity type. The identity type can be one of the following:</p> <ul> <li> <p> <code>EMAIL_ADDRESS</code> – The identity is an email address.</p> </li> <li> <p> <code>DOMAIN</code> – The identity is a domain.</p> </li> <li> <p> <code>MANAGED_DOMAIN</code> – The identity is a domain that is managed by AWS.</p> </li> </ul>"""
    identity_name: NotRequired["capo_pinpoint_email.types.identity.Identity"]
    """<p>The address or domain of the identity.</p>"""
    sending_enabled: "capo_pinpoint_email.types.enabled.Enabled"
    """<p>Indicates whether or not you can send email from the identity.</p> <p>In Amazon Pinpoint, an identity is an email address or domain that you send email from. Before you can send email from an identity, you have to demostrate that you own the identity, and that you authorize Amazon Pinpoint to send email from that identity.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: IdentityInfo) -> dict:
    out: dict = {}
    if "identity_type" in value:
        import capo_pinpoint_email.types.identity_type

        out["IdentityType"] = capo_pinpoint_email.types.identity_type.serialize_json(
            value["identity_type"]
        )
    if "identity_name" in value:
        out["IdentityName"] = value["identity_name"]
    out["SendingEnabled"] = value.get("sending_enabled", False)
    return out


def deserialize_json(data: dict) -> IdentityInfo:
    out: IdentityInfo = {}  # type: ignore[typeddict-item]
    if "IdentityType" in data:
        import capo_pinpoint_email.types.identity_type

        out["identity_type"] = capo_pinpoint_email.types.identity_type.deserialize_json(
            data["IdentityType"]
        )
    if "IdentityName" in data:
        out["identity_name"] = data["IdentityName"]
    if "SendingEnabled" in data:
        out["sending_enabled"] = data["SendingEnabled"]
    else:
        out["sending_enabled"] = False
    return out
