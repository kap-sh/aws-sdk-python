"""Generated from Smithy shape ``com.amazonaws.pinpointemail#PutEmailIdentityDkimAttributesRequest``."""

from typing import TYPE_CHECKING

from typing_extensions import TypedDict

if TYPE_CHECKING:
    import aws_sdk_pinpoint_email.types.enabled
    import aws_sdk_pinpoint_email.types.identity


class PutEmailIdentityDkimAttributesRequest(TypedDict, closed=True):
    email_identity: "aws_sdk_pinpoint_email.types.identity.Identity"
    """<p>The email identity that you want to change the DKIM settings for.</p>"""
    signing_enabled: "aws_sdk_pinpoint_email.types.enabled.Enabled"
    """<p>Sets the DKIM signing configuration for the identity.</p> <p>When you set this value <code>true</code>, then the messages that Amazon Pinpoint sends from the identity are DKIM-signed. When you set this value to <code>false</code>, then the messages that Amazon Pinpoint sends from the identity aren't DKIM-signed.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: PutEmailIdentityDkimAttributesRequest) -> dict:
    out: dict = {}
    out["SigningEnabled"] = value.get("signing_enabled", False)
    return out


def deserialize_json(data: dict) -> PutEmailIdentityDkimAttributesRequest:
    out: PutEmailIdentityDkimAttributesRequest = {}  # type: ignore[typeddict-item]
    if "SigningEnabled" in data:
        out["signing_enabled"] = data["SigningEnabled"]
    else:
        out["signing_enabled"] = False
    return out
