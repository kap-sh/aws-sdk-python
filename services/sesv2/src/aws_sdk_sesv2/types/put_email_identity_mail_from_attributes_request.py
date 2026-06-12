"""Generated from Smithy shape ``com.amazonaws.sesv2#PutEmailIdentityMailFromAttributesRequest``."""

from typing import TYPE_CHECKING, TypedDict

from typing_extensions import NotRequired

if TYPE_CHECKING:
    import aws_sdk_sesv2.types.behavior_on_mx_failure
    import aws_sdk_sesv2.types.identity
    import aws_sdk_sesv2.types.mail_from_domain_name


class PutEmailIdentityMailFromAttributesRequest(TypedDict):
    email_identity: "aws_sdk_sesv2.types.identity.Identity"
    """<p>The verified email identity.</p>"""
    mail_from_domain: NotRequired[
        "aws_sdk_sesv2.types.mail_from_domain_name.MailFromDomainName"
    ]
    """<p> The custom MAIL FROM domain that you want the verified identity to use. The MAIL FROM domain must meet the following criteria:</p> <ul> <li> <p>It has to be a subdomain of the verified identity.</p> </li> <li> <p>It can't be used to receive email.</p> </li> <li> <p>It can't be used in a \"From\" address if the MAIL FROM domain is a destination for feedback forwarding emails.</p> </li> </ul>"""
    behavior_on_mx_failure: NotRequired[
        "aws_sdk_sesv2.types.behavior_on_mx_failure.BehaviorOnMxFailure"
    ]
    """<p>The action to take if the required MX record isn't found when you send an email. When you set this value to <code>UseDefaultValue</code>, the mail is sent using <i>amazonses.com</i> as the MAIL FROM domain. When you set this value to <code>RejectMessage</code>, the Amazon SES API v2 returns a <code>MailFromDomainNotVerified</code> error, and doesn't attempt to deliver the email.</p> <p>These behaviors are taken when the custom MAIL FROM domain configuration is in the <code>Pending</code>, <code>Failed</code>, and <code>TemporaryFailure</code> states.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: PutEmailIdentityMailFromAttributesRequest) -> dict:
    out: dict = {}
    if "mail_from_domain" in value:
        out["MailFromDomain"] = value["mail_from_domain"]
    if "behavior_on_mx_failure" in value:
        import aws_sdk_sesv2.types.behavior_on_mx_failure

        out["BehaviorOnMxFailure"] = (
            aws_sdk_sesv2.types.behavior_on_mx_failure.serialize_json(
                value["behavior_on_mx_failure"]
            )
        )
    return out


def deserialize_json(data: dict) -> PutEmailIdentityMailFromAttributesRequest:
    out: PutEmailIdentityMailFromAttributesRequest = {}  # type: ignore[typeddict-item]
    if "MailFromDomain" in data:
        out["mail_from_domain"] = data["MailFromDomain"]
    if "BehaviorOnMxFailure" in data:
        import aws_sdk_sesv2.types.behavior_on_mx_failure

        out["behavior_on_mx_failure"] = (
            aws_sdk_sesv2.types.behavior_on_mx_failure.deserialize_json(
                data["BehaviorOnMxFailure"]
            )
        )
    return out
