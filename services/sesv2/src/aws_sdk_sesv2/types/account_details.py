"""Generated from Smithy shape ``com.amazonaws.sesv2#AccountDetails``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import aws_sdk_sesv2.types.additional_contact_email_addresses
    import aws_sdk_sesv2.types.contact_language
    import aws_sdk_sesv2.types.mail_type
    import aws_sdk_sesv2.types.review_details
    import aws_sdk_sesv2.types.use_case_description
    import aws_sdk_sesv2.types.website_url


class AccountDetails(TypedDict, closed=True):
    mail_type: NotRequired["aws_sdk_sesv2.types.mail_type.MailType"]
    """<p>The type of email your account is sending. The mail type can be one of the following:</p> <ul> <li> <p> <code>MARKETING</code> – Most of your sending traffic is to keep your customers informed of your latest offering.</p> </li> <li> <p> <code>TRANSACTIONAL</code> – Most of your sending traffic is to communicate during a transaction with a customer.</p> </li> </ul>"""
    website_url: NotRequired["aws_sdk_sesv2.types.website_url.WebsiteURL"]
    """<p>The URL of your website. This information helps us better understand the type of content that you plan to send.</p>"""
    contact_language: NotRequired[
        "aws_sdk_sesv2.types.contact_language.ContactLanguage"
    ]
    """<p>The language you would prefer for the case. The contact language can be one of <code>ENGLISH</code> or <code>JAPANESE</code>.</p>"""
    use_case_description: NotRequired[
        "aws_sdk_sesv2.types.use_case_description.UseCaseDescription"
    ]
    """<p>A description of the types of email that you plan to send.</p>"""
    additional_contact_email_addresses: NotRequired[
        "aws_sdk_sesv2.types.additional_contact_email_addresses.AdditionalContactEmailAddresses"
    ]
    """<p>Additional email addresses where updates are sent about your account review process.</p>"""
    review_details: NotRequired["aws_sdk_sesv2.types.review_details.ReviewDetails"]
    """<p>Information about the review of the latest details you submitted.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: AccountDetails) -> dict:
    out: dict = {}
    if "mail_type" in value:
        import aws_sdk_sesv2.types.mail_type

        out["MailType"] = aws_sdk_sesv2.types.mail_type.serialize_json(
            value["mail_type"]
        )
    if "website_url" in value:
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
    if "review_details" in value:
        import aws_sdk_sesv2.types.review_details

        out["ReviewDetails"] = aws_sdk_sesv2.types.review_details.serialize_json(
            value["review_details"]
        )
    return out


def deserialize_json(data: dict) -> AccountDetails:
    out: AccountDetails = {}  # type: ignore[typeddict-item]
    if "MailType" in data:
        import aws_sdk_sesv2.types.mail_type

        out["mail_type"] = aws_sdk_sesv2.types.mail_type.deserialize_json(
            data["MailType"]
        )
    if "WebsiteURL" in data:
        out["website_url"] = data["WebsiteURL"]
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
    if "ReviewDetails" in data:
        import aws_sdk_sesv2.types.review_details

        out["review_details"] = aws_sdk_sesv2.types.review_details.deserialize_json(
            data["ReviewDetails"]
        )
    return out
