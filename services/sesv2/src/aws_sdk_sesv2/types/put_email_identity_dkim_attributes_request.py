"""Generated from Smithy shape ``com.amazonaws.sesv2#PutEmailIdentityDkimAttributesRequest``."""

from typing import TYPE_CHECKING

from typing_extensions import TypedDict

if TYPE_CHECKING:
    import aws_sdk_sesv2.types.enabled
    import aws_sdk_sesv2.types.identity


class PutEmailIdentityDkimAttributesRequest(TypedDict, closed=True):
    email_identity: "aws_sdk_sesv2.types.identity.Identity"
    """<p>The email identity.</p>"""
    signing_enabled: "aws_sdk_sesv2.types.enabled.Enabled"
    """<p>Sets the DKIM signing configuration for the identity.</p> <p>When you set this value <code>true</code>, then the messages that are sent from the identity are signed using DKIM. If you set this value to <code>false</code>, your messages are sent without DKIM signing.</p>"""


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
