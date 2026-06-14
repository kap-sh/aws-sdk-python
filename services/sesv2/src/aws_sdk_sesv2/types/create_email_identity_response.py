"""Generated from Smithy shape ``com.amazonaws.sesv2#CreateEmailIdentityResponse``."""

from typing import TYPE_CHECKING, TypedDict

from typing_extensions import NotRequired

if TYPE_CHECKING:
    import aws_sdk_sesv2.types.dkim_attributes
    import aws_sdk_sesv2.types.enabled
    import aws_sdk_sesv2.types.identity_type


class CreateEmailIdentityResponse(TypedDict):
    identity_type: NotRequired["aws_sdk_sesv2.types.identity_type.IdentityType"]
    """<p>The email identity type. Note: the <code>MANAGED_DOMAIN</code> identity type is not supported.</p>"""
    verified_for_sending_status: "aws_sdk_sesv2.types.enabled.Enabled"
    r"""<p>Specifies whether or not the identity is verified. You can only send email from verified email addresses or domains. For more information about verifying identities, see the <a href=\"https://docs.aws.amazon.com/pinpoint/latest/userguide/channels-email-manage-verify.html\">Amazon Pinpoint User Guide</a>.</p>"""
    dkim_attributes: NotRequired["aws_sdk_sesv2.types.dkim_attributes.DkimAttributes"]
    """<p>An object that contains information about the DKIM attributes for the identity.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: CreateEmailIdentityResponse) -> dict:
    out: dict = {}
    if "identity_type" in value:
        import aws_sdk_sesv2.types.identity_type

        out["IdentityType"] = aws_sdk_sesv2.types.identity_type.serialize_json(
            value["identity_type"]
        )
    out["VerifiedForSendingStatus"] = value.get("verified_for_sending_status", False)
    if "dkim_attributes" in value:
        import aws_sdk_sesv2.types.dkim_attributes

        out["DkimAttributes"] = aws_sdk_sesv2.types.dkim_attributes.serialize_json(
            value["dkim_attributes"]
        )
    return out


def deserialize_json(data: dict) -> CreateEmailIdentityResponse:
    out: CreateEmailIdentityResponse = {}  # type: ignore[typeddict-item]
    if "IdentityType" in data:
        import aws_sdk_sesv2.types.identity_type

        out["identity_type"] = aws_sdk_sesv2.types.identity_type.deserialize_json(
            data["IdentityType"]
        )
    if "VerifiedForSendingStatus" in data:
        out["verified_for_sending_status"] = data["VerifiedForSendingStatus"]
    else:
        out["verified_for_sending_status"] = False
    if "DkimAttributes" in data:
        import aws_sdk_sesv2.types.dkim_attributes

        out["dkim_attributes"] = aws_sdk_sesv2.types.dkim_attributes.deserialize_json(
            data["DkimAttributes"]
        )
    return out
