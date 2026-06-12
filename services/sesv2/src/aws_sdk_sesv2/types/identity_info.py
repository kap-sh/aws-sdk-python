"""Generated from Smithy shape ``com.amazonaws.sesv2#IdentityInfo``."""

from typing import TYPE_CHECKING, TypedDict

from typing_extensions import NotRequired

if TYPE_CHECKING:
    import aws_sdk_sesv2.types.enabled
    import aws_sdk_sesv2.types.identity
    import aws_sdk_sesv2.types.identity_type
    import aws_sdk_sesv2.types.verification_status


class IdentityInfo(TypedDict):
    identity_type: NotRequired["aws_sdk_sesv2.types.identity_type.IdentityType"]
    """<p>The email identity type. Note: the <code>MANAGED_DOMAIN</code> type is not supported for email identity types.</p>"""
    identity_name: NotRequired["aws_sdk_sesv2.types.identity.Identity"]
    """<p>The address or domain of the identity.</p>"""
    sending_enabled: "aws_sdk_sesv2.types.enabled.Enabled"
    """<p>Indicates whether or not you can send email from the identity.</p> <p>An <i>identity</i> is an email address or domain that you send email from. Before you can send email from an identity, you have to demostrate that you own the identity, and that you authorize Amazon SES to send email from that identity.</p>"""
    verification_status: NotRequired[
        "aws_sdk_sesv2.types.verification_status.VerificationStatus"
    ]
    """<p>The verification status of the identity. The status can be one of the following:</p> <ul> <li> <p> <code>PENDING</code> – The verification process was initiated, but Amazon SES hasn't yet been able to verify the identity.</p> </li> <li> <p> <code>SUCCESS</code> – The verification process completed successfully.</p> </li> <li> <p> <code>FAILED</code> – The verification process failed.</p> </li> <li> <p> <code>TEMPORARY_FAILURE</code> – A temporary issue is preventing Amazon SES from determining the verification status of the identity.</p> </li> <li> <p> <code>NOT_STARTED</code> – The verification process hasn't been initiated for the identity.</p> </li> </ul>"""


# --- restJson1 ser/de ---
def serialize_json(value: IdentityInfo) -> dict:
    out: dict = {}
    if "identity_type" in value:
        import aws_sdk_sesv2.types.identity_type

        out["IdentityType"] = aws_sdk_sesv2.types.identity_type.serialize_json(
            value["identity_type"]
        )
    if "identity_name" in value:
        out["IdentityName"] = value["identity_name"]
    out["SendingEnabled"] = value.get("sending_enabled", False)
    if "verification_status" in value:
        import aws_sdk_sesv2.types.verification_status

        out["VerificationStatus"] = (
            aws_sdk_sesv2.types.verification_status.serialize_json(
                value["verification_status"]
            )
        )
    return out


def deserialize_json(data: dict) -> IdentityInfo:
    out: IdentityInfo = {}  # type: ignore[typeddict-item]
    if "IdentityType" in data:
        import aws_sdk_sesv2.types.identity_type

        out["identity_type"] = aws_sdk_sesv2.types.identity_type.deserialize_json(
            data["IdentityType"]
        )
    if "IdentityName" in data:
        out["identity_name"] = data["IdentityName"]
    if "SendingEnabled" in data:
        out["sending_enabled"] = data["SendingEnabled"]
    else:
        out["sending_enabled"] = False
    if "VerificationStatus" in data:
        import aws_sdk_sesv2.types.verification_status

        out["verification_status"] = (
            aws_sdk_sesv2.types.verification_status.deserialize_json(
                data["VerificationStatus"]
            )
        )
    return out
