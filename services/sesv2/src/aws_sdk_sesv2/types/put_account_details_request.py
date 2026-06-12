"""Generated from Smithy shape ``com.amazonaws.sesv2#PutAccountDetailsRequest``."""

from typing import TYPE_CHECKING, TypedDict

from typing_extensions import NotRequired

from aws_sdk_sesv2.errors import DeserializationError

if TYPE_CHECKING:
    import aws_sdk_sesv2.types.additional_contact_email_addresses
    import aws_sdk_sesv2.types.contact_language
    import aws_sdk_sesv2.types.enabled_wrapper
    import aws_sdk_sesv2.types.mail_type
    import aws_sdk_sesv2.types.use_case_description
    import aws_sdk_sesv2.types.website_url


class PutAccountDetailsRequest(TypedDict):
    mail_type: "aws_sdk_sesv2.types.mail_type.MailType"
    """<p>The type of email your account will send.</p>"""
    website_url: "aws_sdk_sesv2.types.website_url.WebsiteURL"
    """<p>The URL of your website. This information helps us better understand the type of content that you plan to send.</p>"""
    contact_language: NotRequired[
        "aws_sdk_sesv2.types.contact_language.ContactLanguage"
    ]
    """<p>The language you would prefer to be contacted with.</p>"""
    use_case_description: NotRequired[
        "aws_sdk_sesv2.types.use_case_description.UseCaseDescription"
    ]
    """<p>A description of the types of email that you plan to send.</p>"""
    additional_contact_email_addresses: NotRequired[
        "aws_sdk_sesv2.types.additional_contact_email_addresses.AdditionalContactEmailAddresses"
    ]
    """<p>Additional email addresses that you would like to be notified regarding Amazon SES matters.</p>"""
    production_access_enabled: NotRequired[
        "aws_sdk_sesv2.types.enabled_wrapper.EnabledWrapper"
    ]
    """<p>Indicates whether or not your account should have production access in the current Amazon Web Services Region.</p> <p>If the value is <code>false</code>, then your account is in the <i>sandbox</i>. When your account is in the sandbox, you can only send email to verified identities. </p> <p>If the value is <code>true</code>, then your account has production access. When your account has production access, you can send email to any address. The sending quota and maximum sending rate for your account vary based on your specific use case.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: PutAccountDetailsRequest) -> dict:
    out: dict = {}
    import aws_sdk_sesv2.types.mail_type

    out["MailType"] = aws_sdk_sesv2.types.mail_type.serialize_json(value["mail_type"])
    out["WebsiteURL"] = value["website_url"]
    if "contact_language" in value:
        import aws_sdk_sesv2.types.contact_language

        out["ContactLanguage"] = aws_sdk_sesv2.types.contact_language.serialize_json(
            value["contact_language"]
        )
    if "use_case_description" in value:
        out["UseCaseDescription"] = value["use_case_description"]
    if "additional_contact_email_addresses" in value:
        import aws_sdk_sesv2.types.additional_contact_email_addresses

        out["AdditionalContactEmailAddresses"] = (
            aws_sdk_sesv2.types.additional_contact_email_addresses.serialize_json(
                value["additional_contact_email_addresses"]
            )
        )
    if "production_access_enabled" in value:
        out["ProductionAccessEnabled"] = value["production_access_enabled"]
    return out


def deserialize_json(data: dict) -> PutAccountDetailsRequest:
    out: PutAccountDetailsRequest = {}  # type: ignore[typeddict-item]
    if "MailType" in data:
        import aws_sdk_sesv2.types.mail_type

        out["mail_type"] = aws_sdk_sesv2.types.mail_type.deserialize_json(
            data["MailType"]
        )
    else:
        raise DeserializationError("PutAccountDetailsRequest.mail_type required")
    if "WebsiteURL" in data:
        out["website_url"] = data["WebsiteURL"]
    else:
        raise DeserializationError("PutAccountDetailsRequest.website_url required")
    if "ContactLanguage" in data:
        import aws_sdk_sesv2.types.contact_language

        out["contact_language"] = aws_sdk_sesv2.types.contact_language.deserialize_json(
            data["ContactLanguage"]
        )
    if "UseCaseDescription" in data:
        out["use_case_description"] = data["UseCaseDescription"]
    if "AdditionalContactEmailAddresses" in data:
        import aws_sdk_sesv2.types.additional_contact_email_addresses

        out["additional_contact_email_addresses"] = (
            aws_sdk_sesv2.types.additional_contact_email_addresses.deserialize_json(
                data["AdditionalContactEmailAddresses"]
            )
        )
    if "ProductionAccessEnabled" in data:
        out["production_access_enabled"] = data["ProductionAccessEnabled"]
    return out
